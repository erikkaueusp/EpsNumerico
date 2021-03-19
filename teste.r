g = function(t,y,z){
  return(z - y +t^3 -3*t^2 +6*t)
}
rk4 = function(ti,yi,zi,h){
 k1y = h*zi
 k1z = h*g(ti,yi,zi)
 k2y = h*(zi + k1z/2)
 k2z = h*g(ti + h/2, yi + k1y/2, zi + k1z/2)
 k3y = h*(zi + k2z/2)
 k3z = h*g(ti + h/2, yi + k2y/2, zi + k2z/2)
 k4y = h*(zi + k3z)
 k4z = h*g(ti + h, yi + k3y, zi + k3z)
 yi = yi + (k1y + 2*k2y + 2*k3y + k4y)/6
 zi = zi + (k1z + 2*k2z + 2*k3z + k4z)/6
 ti = ti + h
}