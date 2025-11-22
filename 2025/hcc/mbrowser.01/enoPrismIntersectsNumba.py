# Numba-accelerated point-in-quads query mechanisms
# Co-evolved by Brygg Ullmer with CoPilot
# November 2025

import numpy as np
import numba as nb

################## _cross ##################

@nb.njit
def _cross(ax, ay, bx, by):
    # int64 intermediates to avoid overflow of products
    return np.int64(ax) * np.int64(by) - np.int64(ay) * np.int64(bx)

################## point in quads, batch ##################

@nb.njit(parallel=True)
def point_in_quads_batch(px, py, quads, bounds):
    """
    Batch point-in-convex-quad test with AABB early reject.

    Parameters
    ----------
    px, py : int
        Query point (2D integer).
    quads : (N, 4, 2) int32/int64
        Vertices per quad (either CCW or CW). Each row: [[x0,y0],[x1,y1],[x2,y2],[x3,y3]]
    bounds : (N, 4) int32/int64
        [xmin, ymin, xmax, ymax] per quad.

    Returns
    -------
    out : (N,) int8
        0 = outside, 1 = inside, 2 = on-edge (collinear + within segment).
    """
    n = quads.shape[0]
    out = np.zeros(n, dtype=np.int8)

    for i in nb.prange(n):
        xmin = bounds[i, 0]
        ymin = bounds[i, 1]
        xmax = bounds[i, 2]
        ymax = bounds[i, 3]

        # Pass 1: AABB filter
        if (px < xmin) or (px > xmax) or (py < ymin) or (py > ymax):
            out[i] = 0
            continue

        # Fetch vertices
        x0 = quads[i, 0, 0]; y0 = quads[i, 0, 1]
        x1 = quads[i, 1, 0]; y1 = quads[i, 1, 1]
        x2 = quads[i, 2, 0]; y2 = quads[i, 2, 1]
        x3 = quads[i, 3, 0]; y3 = quads[i, 3, 1]

        # Pass 2: Half-space (orientation) tests for a convex quad
        # c_k = cross(edge_k, point_delta_k)
        c0 = _cross(x1 - x0, y1 - y0, px - x0, py - y0)
        c1 = _cross(x2 - x1, y2 - y1, px - x1, py - y1)
        c2 = _cross(x3 - x2, y3 - y2, px - x2, py - y2)
        c3 = _cross(x0 - x3, y0 - y3, px - x3, py - y3)

        # On-edge if any cross-product is 0 AND projected within segment;
        # the segment inclusion check below is optional—here we return 2
        # if any cross == 0 and the point passes the inside test.
        on = (c0 == 0) or (c1 == 0) or (c2 == 0) or (c3 == 0)

        # Inside for convex polygons: all cross-products have the same sign.
        inside_pos = (c0 >= 0) and (c1 >= 0) and (c2 >= 0) and (c3 >= 0)
        inside_neg = (c0 <= 0) and (c1 <= 0) and (c2 <= 0) and (c3 <= 0)
        inside = inside_pos or inside_neg

        out[i] = np.int8(2 if (on and inside) else (1 if inside else 0))

    return out

################## compute AABBs from quads##################

def compute_aabbs_from_quads(quads: np.ndarray) -> np.ndarray:
    """
    Build [xmin, ymin, xmax, ymax] for each quad.
    quads: (N,4,2) int32/int64
    """
    xs = quads[..., 0]
    ys = quads[..., 1]
    xmin = xs.min(axis=1)
    xmax = xs.max(axis=1)
    ymin = ys.min(axis=1)
    ymax = ys.max(axis=1)
    return np.stack((xmin, ymin, xmax, ymax), axis=1).astype(quads.dtype)

################## ensure CCW quads ##################

def ensure_ccw_quads(quads: np.ndarray) -> np.ndarray:
    """
    Ensure each quad is CCW-ordered (shoelace area > 0). Returns a copy if any flipped.
    """
    xs = quads[..., 0]; ys = quads[..., 1]
    # Shoelace area: sum(x_i*y_{i+1} - y_i*x_{i+1})
    area = (xs[:,0]*ys[:,1] - ys[:,0]*xs[:,1] +
            xs[:,1]*ys[:,2] - ys[:,1]*xs[:,2] +
            xs[:,2]*ys[:,3] - ys[:,2]*xs[:,3] +
            xs[:,3]*ys[:,0] - ys[:,3]*xs[:,0])
    ccw = (area > 0)
    if np.all(ccw):
        return quads
    out = quads.copy()
    to_flip = np.where(~ccw)[0]
    # Reverse vertex order for those quads
    out[to_flip] = out[to_flip, ::-1, :]
    return out

################## quads from list ##################

def quads_from_list(quad_list, dtype=np.int32):
    """
    quad_list: list of length N; each element is an iterable of 4 (x,y) pairs
    Returns: np.ndarray of shape (N,4,2), dtype=dtype (C-contiguous)
    """
    arr = np.asarray(quad_list, dtype=dtype)
    if arr.ndim != 3 or arr.shape[1:] != (4, 2):
        raise ValueError(f"Expected shape (N,4,2), got {arr.shape}")
    return np.ascontiguousarray(arr)

# Usage
#quads = quads_from_list(quad_list, dtype=np.int32)

### end ###
