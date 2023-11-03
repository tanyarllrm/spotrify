import Sortable from 'sortablejs';
import Sortable.min.js from 'sortablejs';

const tracks = document.getElementById('tracks');
   let sortable = Sortable.create(tracks, {
});

let sortable = Sortable.create(tracks, {
    handle: '.handle',
});