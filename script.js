
  
  (function(){
    const container = document.getElementById('pookalam');
    if(!container) return;
    // read the --petals CSS variable (unitless)
    const style = getComputedStyle(container);
    const petalsCount = parseInt(style.getPropertyValue('--petals')) || 12;

    // if there are already petal nodes, do nothing (so manual mode works)
    if(container.querySelector('.petal-ring')) return;
    const ring=document.createElement('div');
    ring.className='petal-ring';
    
    for(let i = 0; i < petalsCount; i++){
      const d = document.createElement('div');
      d.className = 'petal';
      // set the index used by CSS to compute rotation
      d.style.setProperty('--i', i);
      ring.appendChild(d);
    }
    container.appendChild(ring);
  })();
