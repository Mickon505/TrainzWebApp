let iframe = document.getElementById("iframediv");
let row_1 = document.getElementById("firstRow");
let row_2 = document.getElementById("secondRow");

window.onresize = () => {
    if (window.innerWidth < 935){
        row_2.appendChild(iframe);
    }
    else {
        row_1.appendChild(iframe);
    }
}