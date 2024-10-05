//import jsyaml from 'js-yaml';

console.log('a');

var ta1 = document.getElementById("ta1");

var yamlText = `
  - hello
  - world
  `;

  // Parse YAML to JavaScript object
//var doc = jsyaml.load(yamlText);

async function getYaml() {
  const yfn = './hello1.yaml';
  //const yfn = 'https://people.computing.clemson.edu/~bullmer/code/js/helloH2.yaml';
  //const yfn = '/bullmer/code/js/helloH2.yaml';
  const f1 = await fetch(yfn);
  const yt = await f1.text();
  console.log(yt);
  const y2 = jsyaml.load(yt);
  console.log(y2);
  return y2;
}

async function buildButtons() {
  const y = await getYaml();
  console.log("buildButtons")
  console.log(y)
  var ta1 = document.getElementById("ta1");

  const yLen = y.length;
  for (let i=0; i<yLen; i++) {
    console.log(y[i]);
    ta1.value += y[i] + ' ';
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

