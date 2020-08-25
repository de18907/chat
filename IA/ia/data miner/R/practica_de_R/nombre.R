va = seq(3,5,length.out = 100)
vb = 4
tm = (1:100)/1000
vc = -vb*2*va^3
dft = data.frame(tm,va,vc)
dft2 = data.frame(dft,vb)

icc = function(v,nc = 0.95,n = 100)
{ vg = v/n
  aux = sqrt(vg*(1-vg)/n)
  fc = qnorm((1 + nc)/2)
  return(vg + c(-1,1)*fc*aux)
}