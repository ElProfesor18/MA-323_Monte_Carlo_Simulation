function X = normal_gen(Z,mu,sigma,ro)
A = [sqrt(sigma(1,1))  0 ; ro*sqrt(sigma(2,2))  sqrt(1-ro^2)*sqrt(sigma(2,2)) ];
X = mu + A*Z;
end