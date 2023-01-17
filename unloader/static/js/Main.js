const btn_close = document.getElementById('btn-close');
const error = document.getElementById('error');

function close_pop_up() {
    btn_close.addEventListener('click', () => {
        error.style.cssText = 'display: none;'
    })
}
close_pop_up();

