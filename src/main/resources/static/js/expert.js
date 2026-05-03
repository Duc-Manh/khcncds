function toggleExpertRegistration() {
         const searchTools = document.getElementById('expert-search-tools');
         const grid = document.getElementById('expert-grid');
         const pagination = document.getElementById('expert-pagination');
         const form = document.getElementById('expert-regis-form');

         if (form.classList.contains('hidden')) {
            // Hide list elements, show form
            searchTools.classList.add('hidden');
            grid.classList.add('hidden');
            pagination.classList.add('hidden');
            form.classList.remove('hidden');
         } else {
            // Hide form, show list elements
            form.classList.add('hidden');
            searchTools.classList.remove('hidden');
            grid.classList.remove('hidden');
            pagination.classList.remove('hidden');
         }
      }