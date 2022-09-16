function getelement(id) {
    return document.getElementById(id)
}
const searchsupplier1button = getelement('searchsupplier1')
const searchsupplierform1 = getelement('searchsupplierform1')
let show = true
if (
    searchsupplierform1


) {
    searchsupplierform1.hidden = show
}


if (searchsupplierform1) {
    console.log(searchsupplier1button)
    searchsupplier1button.addEventListener('click', function () {
        show = !show
        searchsupplierform1.hidden = show
    })
}

function redirect() {
    console.log('click')
    window.location.href = 'http://127.0.0.1:5500/component/supplierList/editsupplier.html'

}
function addsupplier() {
    console.log('click')
    window.location.href = 'http://127.0.0.1:5500/component/supplierList/addsupplier.html'
}
function editpurchaserequest() {
    console.log('click')
    window.location.href = 'http://127.0.0.1:5500/component/supplierList/addsupplier.html'
}
function createpurchaserequest() {
    console.log('click')
    window.location.href = 'http://127.0.0.1:5500/purchase_request/createpurchaserequest.html'
}


const addItembutton = getelement('addItembutton')
console.log(addItembutton)
if (
    addItembutton
) {
    addItembutton.addEventListener('click', addItem)
}

function myFunction() {
    var x = document.getElementById("myDIV");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}
let menuitem=getelement('menuitem')
const togglemenu = getelement('togglemenu')
console.log(togglemenu)
let hidden=false
if (
    togglemenu
) {
    togglemenu.hidden=true
    togglemenu.addEventListener('click', function(){console.log('toggle')
    hidden=!hidden
menuitem.hidden=hidden
})
}
/*window.addEventListener('resize', function(event){
    var newWidth = window.innerWidth;
    var newHeight = window.innerHeight;
    console.log(newWidth, togglemenu.hidden)
    if(newWidth<1000) {
        togglemenu.hidden=false
        menuitem.hidden=true
    }
    else{
        togglemenu.hidden=true
        menuitem.hidden=false
    }
});*/

