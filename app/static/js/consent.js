(function(){
  const key = 'cookie_consent_v1';
  if (localStorage.getItem(key)) return;
  const bar = document.createElement('div');
  bar.style.position = 'fixed';
  bar.style.bottom = '0';
  bar.style.left = '0';
  bar.style.right = '0';
  bar.style.background = '#212529';
  bar.style.color = '#fff';
  bar.style.padding = '12px';
  bar.style.display = 'flex';
  bar.style.justifyContent = 'center';
  bar.style.gap = '12px';
  bar.style.zIndex = '9999';
  bar.innerHTML = '<span>We use cookies for analytics and improvements.</span>'+
    '<button id="consent-accept" class="btn btn-sm btn-primary">Accept</button>'+
    '<button id="consent-decline" class="btn btn-sm btn-secondary">Decline</button>';
  document.body.appendChild(bar);
  function close(){ document.body.removeChild(bar); }
  document.getElementById('consent-accept').onclick = function(){ localStorage.setItem(key, 'accepted'); close(); };
  document.getElementById('consent-decline').onclick = function(){ localStorage.setItem(key, 'declined'); close(); };
})();
