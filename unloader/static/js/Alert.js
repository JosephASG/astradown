const $formUnload = document.getElementById('form-unload');
const btn_download = document.getElementById('#download')
const loader_download = document.querySelector('.loader-download')
const btn_xmark_close = document.querySelector('.xmark')
const clickBtn = document.getElementById("clickBtn");
const popup = document.getElementById("popup");
const closeBtn = document.getElementById("closeBtn");

function alert_pop() {
    $formUnload.addEventListener('submit', (e) => {
        // Swal.fire(
        //     {
        //         titleText: 'No cierres Astradown',
        //         text: 'Tu video está siendo descargado...',
        //         icon: 'success',
        //         confirmButtonText: 'Ok',
        //     }
        // )
        loader_download.style.display = 'block';
        btn_xmark_close.addEventListener('click', () => {
            loader_download.style.display = 'none';
        });
        loader_download.addEventListener('click', () => {
            loader_download.style.display = 'none';
        });
    })
}
alert_pop();