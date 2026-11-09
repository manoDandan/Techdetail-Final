const cableDemo = document.querySelector('.cable-demo');
const cableFeedback = document.querySelector('#cable-feedback');
document.querySelectorAll('[data-mode]').forEach(button => {
  button.addEventListener('click', () => {
    cableDemo.dataset.cableState = button.dataset.mode;
    document.querySelectorAll('[data-mode]').forEach(option => option.setAttribute('aria-pressed', String(option === button)));
    cableFeedback.textContent = button.dataset.mode === 'organized'
      ? 'Rotas definidas. Cabos agrupados. Hardware em destaque.'
      : 'Fios cruzando o gabinete e ocupando o espaço dos componentes.';
  });
});

const mobileMenu = document.querySelector('.mobile-menu');
mobileMenu.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => { mobileMenu.open = false; });
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && mobileMenu.open) {
    mobileMenu.open = false;
    mobileMenu.querySelector('summary').focus();
  }
});
document.addEventListener('click', event => {
  if (mobileMenu.open && !mobileMenu.contains(event.target)) mobileMenu.open = false;
});
