function Z = box_muller(num,u1,u2)
r = [];
for j=1:num
    r(j) = -2*log(u1(j));
end

v = [];
for j=1:num
    v(j) = 2*pi*u2(j);
end

z1 = [];
z2 = [];
for j = 1:num
    z1(j) = sqrt(r(j))*cos(v(j));
    z2(j) = sqrt(r(j))*sin(v(j));
end
Z = [z1;z2];
end