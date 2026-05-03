const modal = document.getElementById('eval-modal');
        const modalContent = document.getElementById('eval-modal-content');
        
        function openEvalModal(id) {
            document.getElementById('modal-hs-id').textContent = id;
            modal.classList.remove('hidden');
            // Trigger reflow
            void modal.offsetWidth;
            modal.classList.remove('opacity-0');
            modalContent.classList.remove('scale-95');
            document.body.style.overflow = 'hidden'; // Prevent background scrolling
        }

        function closeEvalModal() {
            modal.classList.add('opacity-0');
            modalContent.classList.add('scale-95');
            setTimeout(() => {
                modal.classList.add('hidden');
                document.body.style.overflow = 'auto';
            }, 300);
        }

        // Close on clicking outside
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                closeEvalModal();
            }
        });