window.onload = () => {
  let testing = document.querySelector(".testing");
  let fileInput = document.querySelector(".file_adder");
  testing.style.display = "none";
  fileInput.style.display = "none";
};

let button = document.querySelector("button.ui.button");

const openGUI = () => {
  let testing = document.querySelector(".testing");
  if (testing.style.display === "none") {
    testing.style.display = "block";
  } else {
    testing.style.display = "none";
  }
};

const Submit = () => {
  openGUI();
  let inputText = document.querySelector(".center_text");
  console.log(inputText.value);
  let outputText = document.querySelector(".output_text");
  outputText.innerHTML = inputText.value;

  let fileInput = document.querySelector(".file_adder");
  if (fileInput.files && fileInput.files[0]) {
    file = URL.createObjectURL(fileInput.files[0]);
    let filePreview = document.querySelector("#file-preview");
    filePreview.src = file;
  }
};
