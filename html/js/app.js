const tbody = document.getElementsByTagName("table")[0].childNodes[3];
let rows = tbody.childNodes;
rows.forEach((element, index) => {
  if (index % 2 == 1) {
    let cell = element.childNodes[9];
    let cell_to_float = parseFloat(cell.innerText);
    console.log(cell_to_float);
    if (cell_to_float < 0) {
      cell.classList.add("negValue");
      console.log(cell);
      console.log("change class");
    }
  }
});
