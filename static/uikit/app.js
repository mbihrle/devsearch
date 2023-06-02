// Invoke Functions Call on Document Loaded
console.log('this is the right script (in static folder)');
// document.addEventListener('DOMContentLoaded', function () {
//     hljs.highlightAll();
// });

let alertWrapper = document.querySelectorAll('.alert');
let alertClose = document.querySelectorAll('.alert__close');

if (alertWrapper) {
    for (let i = 0; i < alertClose.length; i++) {
        alertClose[i].addEventListener('click', () => {
            alertWrapper[i].style.display = 'none';
        });
    }
}
