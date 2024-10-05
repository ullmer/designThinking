// Code by Brygg Ullmer, Clemson University
// Begun 2024-10-02
// (First day coding JavaScript, so errors doubtless to come)

console.log('a');

// Parse YAML to JavaScript object

async function getYaml() {
  const  yfn = './readyNC.yaml';
  const  f1  = await fetch(yfn);
  const  yt  = await f1.text(); console.log(yt);
  const  yd  = jsyaml.load(yt); console.log(yd);
  return yd;
}

async function buildButtons() {
  const y = await getYaml();
  console.log("buildButtons")
  console.log(y)
  var bc1 = document.getElementById("buttonContainer");

  ycat = y['categories']

  const yLen = ycat.length;
  for (let i=0; i<yLen; i++) {
    name   = ycat[i]['name']
    abbrev = ycat[i]['a']
    console.log(ycat[i]);
    const btn = document.createElement('button');
    btn.innerText   = name;
    btn.style.width = 50;
    bc1.appendChild(btn);
  }
}

buildButtons();

// Function to create buttons
function createButtons(buttons) {
    const container = document.getElementById('buttonContainer');
    buttons.forEach(button => {
        const btn = document.createElement('button');
        btn.innerText = button.label;
        container.appendChild(btn);
    });
}

// Wait for the DOM to load before creating buttons
//document.addEventListener('DOMContentLoaded', () => {
//    createButtons(data.buttons);
//});

