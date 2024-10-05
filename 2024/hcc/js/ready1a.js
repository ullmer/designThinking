//import jsyaml from 'js-yaml';

console.log('a');

var ta1 = document.getElementById("ta1");

var yamlText = `
  - hello
  - world
  `;

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
  var ta1 = document.getElementById("ta1");

  ycat = y['categories']

  const yLen = ycat.length;
  for (let i=0; i<yLen; i++) {
    name = ycat[i]['name']
    console.log(ycat[i]);
    ta1.value += name + '\n';
  }
}

buildButtons();

ta1.value += "b\n";

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

