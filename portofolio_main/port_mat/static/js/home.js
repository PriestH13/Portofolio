function toggleMenu() {
    document.querySelector('.nav').classList.toggle('active');
  }

function toggleMenu() {
    const nav = document.querySelector('.nav');
    nav.classList.toggle('active');
  }

  document.addEventListener('DOMContentLoaded', function() {
    
    if (typeof lightGallery === 'undefined') {
        console.error('LightGallery non è caricato. Verifica gli script in home.html.');
        return;
    }

    
    const galleries = document.querySelectorAll('.lightgallery');
    
    if (galleries.length === 0) {
        console.warn('Nessuna galleria trovata con classe "lightgallery".');
        return;
    }

    galleries.forEach((gallery, index) => {
        try {
            const links = gallery.querySelectorAll('a');
            if (links.length === 0) {
                console.warn(`La galleria ${gallery.id} non contiene link validi.`);
                return;
            }

            lightGallery(gallery, {
                selector: 'a',
                plugins: [
                    typeof lgZoom !== 'undefined' ? lgZoom : null,
                    typeof lgThumbnail !== 'undefined' ? lgThumbnail : null
                ].filter(plugin => plugin), 
                speed: 500,
                thumbnail: true,
                zoom: true,
                mode: 'lg-slide',
                licenseKey: '', 
                download: false, 
                counter: true, 
                preload: 2, 
                addClass: 'lg-custom', 
                onInit: () => {
                    console.log(`Galleria ${gallery.id} inizializzata con successo.`);
                },
                onBeforeSlide: (detail) => {
                    console.log(`Passaggio all'immagine ${detail.index + 1} nella galleria ${gallery.id}`);
                }
            });
        } catch (error) {
            console.error(`Errore nell'inizializzazione della galleria ${gallery.id}:`, error);
        }
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("descriptionModal");
    const modalText = document.getElementById("modal-description-text");
    const closeModal = document.querySelector(".close-modal");

    document.querySelectorAll(".toggle-description-btn").forEach(btn => {
        btn.addEventListener("click", function () {
            const description = this.getAttribute("data-description");
            modalText.textContent = description;
            modal.style.display = "block";
        });
    });

    closeModal.addEventListener("click", function () {
        modal.style.display = "none";
    });

    window.addEventListener("click", function (e) {
        if (e.target === modal) {
            modal.style.display = "none";
        }
    });
});

        
        document.addEventListener('DOMContentLoaded', function() {
            const buttons = document.querySelectorAll('.toggle-description-btn');
            const modal = document.getElementById('descriptionModal');
            const modalText = document.getElementById('modal-description-text');
            const closeModal = document.querySelector('.close-modal');

            buttons.forEach(button => {
                button.addEventListener('click', function() {
                    modalText.textContent = this.getAttribute('data-description');
                    modal.style.display = 'block';
                });
            });

            closeModal.addEventListener('click', function() {
                modal.style.display = 'none';
            });

            window.addEventListener('click', function(event) {
                if (event.target === modal) {
                    modal.style.display = 'none';
                }
            });
        });