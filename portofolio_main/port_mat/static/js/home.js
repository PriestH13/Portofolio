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