window.onload=function(){$("form").css('display','none');$("#jieshao").css('display','block');}
function peng(obj){$('#erzi').slideReveal("hide");if(obj.id!="erzi1"){$("form").css('display','none');document.getElementById(obj.id+1).style.display="block";}}
function peng1(obj){document.getElementById(obj.id+1).style.display="block";}
function shuzu(s,r,n,m){var arr1=[];for(var i=0;i<n;i++){var tb=i+1;arr1[i]=[];for(var j=0;j<m;j++){var tc=j+1;var d=parseFloat(document.getElementById("Z"+s+r+tb+tc).value);arr1[i][j]=d;}}
return arr1;}
function shuzu1(s,r,n,m){var arr1=[];for(var i=0;i<n;i++){var tb=i+1;arr1[i]=[];for(var j=0;j<m;j++){var tc=j+1;if(tc!=3&&tc!=6&&tc!=9)
var d=parseFloat(document.getElementById("Z"+s+r+tb+tc).value);d=Number(d);arr1[i][j]=d;}}
return arr1;}
function fatxzh(r,n,m,y){var w=[];for(var i=0;i<n.length;i++){var k=r[i]*m[i]/100;k=k.toFixed(8);w[i]=[];for(var p=0;k<1;p++){k*=10;k=k.toFixed(8);}
p=p.toFixed(0);for(var j=0;j<n[i].length;j++){var e=n[i][j]*r[i]/y[i];e=e.toFixed(p);w[i][j]=Number(e);}}
return w;}
function fatxsr(s,r,n,m,g){for(var i=0;i<n;i++){var tb=i+1;for(var j=0;j<m;j++){var tc=j+1;document.getElementById("OP"+s+r+tb+tc).innerHTML=g[i][j];}}}
function zldqsr(s,r,n,m,g){for(var i=0;i<n;i++){var tb=i+1;for(var j=0;j<m;j++){var tc=j+1;document.getElementById("OPP"+s+r+tb+tc).innerHTML=g[i][j];}}}