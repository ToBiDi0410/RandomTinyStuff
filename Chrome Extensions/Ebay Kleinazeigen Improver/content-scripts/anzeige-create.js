console.log("Ebay Kleinanzeigen Improver --> anzeige-create.js");

if(url_vars["auto_insert"] != null && url_vars["auto_insert"] != "" && url_vars["auto_insert"] != 1) {
  setTimeout(async function() {
    console.log("Automatically Inserting Infos...");
    loadAllData(url_vars["auto_insert"]);
    insertData();
  },1000);
}

function loadAllData(id) {
  title = localStorage.getItem(id + "_title");
  price = localStorage.getItem(id + "_price");
  description = localStorage.getItem(id + "_desc");
}

function insertData() {
  document.getElementById("postad-title").value = title;
  document.getElementById("pstad-descrptn").value = description;
  if(isNaN(price)) {
    if(price.includes("VB")) {
      setToVB();
    }
    if(price.replace("VB","") != "" || price.replace("VB","") != null) {
      if(!isNaN(price.replace("VB",""))) {
        document.getElementById("pstad-price").value = price.replace("VB","");
      }
    }
  } else {
    setToFestpreis();
    document.getElementById("pstad-price").value = price;
  }
}

function setToFestpreis()  { document.getElementById("priceType1").click(); }

function setToVB() { document.getElementById("priceType2").click(); }

function setToVerschenken() { document.getElementById("priceType3").click(); }