# https://www.activestate.com/resources/quick-reads/how-to-display-data-in-a-table-using-tkinter/

import tkinter as tk
import tksheet
top = tk.Tk()
sheet = tksheet.Sheet(top, theme='dark blue')
sheet.grid()
sheet.default_column_width(50)
sheet.set_sheet_data([[f"{ri+cj}" for cj in range(9)] for ri in range(9)])
# table enable choices listed below:
sheet.enable_bindings(("single_select",
                       "row_select",
                       "column_width_resize",
                       "arrowkeys",
                       "right_click_popup_menu",
                       "rc_select",
                       "rc_insert_row",
                       "rc_delete_row",
                       "copy",
                       "cut",
                       "paste",
                       "delete",
                       "undo",
                       "edit_cell"))
top.mainloop()

### end ###
