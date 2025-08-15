(function(){
  const btn = document.querySelector('[data-chat-button]');
  if(!btn) return;
  btn.addEventListener('click', function(){
    const panel = document.querySelector('[data-chat-panel]');
    if(panel) panel.classList.toggle('open');
  });
})();
