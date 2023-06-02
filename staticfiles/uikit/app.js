// Invoke Functions Call on Document Loaded
console.log('hello script3');
document.addEventListener('DOMContentLoaded', function () {
    hljs.highlightAll();
});

let alertWrapper = document.querySelector('.alert');
let alertClose = document.querySelector('.alert__close');

if (alertWrapper) {
    console.log('Alert Wrapper clicked');
    alertClose.addEventListener(
        'click',
        () => (alertWrapper.style.display = 'none')
    );
}
