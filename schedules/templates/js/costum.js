document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.view-full-description').forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const fullDescription = this.getAttribute('data-description');
            const modalBody = document.querySelector('#descriptionModal .modal-body');
            modalBody.textContent = fullDescription;
            const descriptionModal = new bootstrap.Modal(document.getElementById('descriptionModal'));
            descriptionModal.show();
        });
    });
});
