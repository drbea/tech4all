
// Initialize Bootstrap popovers on hover
document.querySelectorAll('[data-bs-toggle="popover"]').forEach(function (popover) {
var popoverInstance = new bootstrap.Popover(popover, {
    trigger: 'hover',
    delay: { show: 200, hide: 400 }
});
});