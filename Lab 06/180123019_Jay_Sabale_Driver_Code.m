% To Run the following code in MATLAB, the files box_muller.m 
% and normal_generation.m are functions.
% This is just the driver code.
% Save the functions first and then 
% run the following code as a single command!

clear
clc
% using box muller to generate Z = [z1 z2]
num = 1000;
U1 = rand(1,1000);
U2 = rand(1,1000);
Z = box_muller(num,U1,U2);

a = -0.5;
mu = [5;8];
sigma = [1 2*a;2*a 4];
X = normal_gen(Z,mu,sigma,a);
%ques2
figure;
hist3(X',[15 15])
title('Histogram for -0.5')
figure;
%simulated
subplot(2,1,1);
x=X(1,:);
y=X(2,:);
surfc(hist3(X',[10 10])/(1000*((max(x)-min(x))/10)*((max(y)-min(y))/10)));
title('Simulated for -0.5')
%actual
subplot(2,1,2);
x=X(1,:);
y=X(2,:);
x1 = min(x):.1:max(x); 
x2 = min(y):.1:max(y);
[M1,M2] = meshgrid(x1,x2);
F = mvnpdf([M1(:) M2(:)],mu',sigma);
F = reshape(F,length(x2),length(x1));
surf(x1,x2,F);
% caxis([min(F(:))-.5*range(F(:)),max(F(:))]);
axis([min(x) max(x) min(y) max(y) 0 .15])
xlabel('X1'); ylabel('X2'); zlabel('Probability Density');
title('Actual Density')
%marginal
frange=min(X(1,:)):0.05:max(X(1,:));
range=-20:0.05:20;
rangemid=range/2;
y=(1/(sqrt(2*pi)*sqrt(1)))*exp(-((rangemid-5).*(rangemid-5)/(2*1)));
count=histc(X(1,:),frange);
count=count/(0.05*1000);

figure;
hold on;
plot(frange,count);
title('Marginal Density of x1 for a = -0.5');
plot(rangemid,y,'r','Linewidth',3);
xlabel('Value of x');
ylabel('Density');
hold off;

frange=min(X(2,:)):0.05:max(X(2,:));
range=-20:0.05:30;
rangemid=range/2;
y=(1/(sqrt(2*pi)*sqrt(4)))*exp(-((rangemid-8).*(rangemid-8)/(2*4)));
count=histc(X(2,:),frange);
count=count/(0.05*1000);

figure;
hold on;
plot(frange,count);
title('Marginal Density of x2 for a = -0.5');
plot(rangemid,y,'r','Linewidth',3);
xlabel('Value of x');
ylabel('Density');
hold off;


a = 0;
mu = [5;8];
sigma = [1 2*a;2*a 4];
X = normal_gen(Z,mu,sigma,a);
%ques2
figure;
hist3(X',[15 15])
title('Histogram for 0')
figure;
%simulated
subplot(2,1,1);
x=X(1,:);
y=X(2,:);
surfc(hist3(X',[10 10])/(1000*((max(x)-min(x))/10)*((max(y)-min(y))/10)));
title('Simulated for 0')
%actual
subplot(2,1,2);
x=X(1,:);
y=X(2,:);
x1 = min(x):.1:max(x); 
x2 = min(y):.1:max(y);
[M1,M2] = meshgrid(x1,x2);
F = mvnpdf([M1(:) M2(:)],mu',sigma);
F = reshape(F,length(x2),length(x1));
surf(x1,x2,F);
% caxis([min(F(:))-.5*range(F(:)),max(F(:))]);
axis([min(x) max(x) min(y) max(y) 0 .15])
xlabel('X1'); ylabel('X2'); zlabel('Probability Density');
title('Actual Density')
%marginal
frange=min(X(1,:)):0.05:max(X(1,:));
range=-20:0.05:20;
rangemid=range/2;
y=(1/(sqrt(2*pi)*sqrt(1)))*exp(-((rangemid-5).*(rangemid-5)/(2*1)));
count=histc(X(1,:),frange);
count=count/(0.05*1000);

figure;
hold on;
plot(frange,count);
title('Marginal Density of x1 for a = 0');
plot(rangemid,y,'r','Linewidth',3);
xlabel('Value of x');
ylabel('Density');
hold off;

frange=min(X(2,:)):0.05:max(X(2,:));
range=-20:0.05:30;
rangemid=range/2;
y=(1/(sqrt(2*pi)*sqrt(4)))*exp(-((rangemid-8).*(rangemid-8)/(2*4)));
count=histc(X(2,:),frange);
count=count/(0.05*1000);

figure;
hold on;
plot(frange,count);
title('Marginal Density of x2 for a = 0');
plot(rangemid,y,'r','Linewidth',3);
xlabel('Value of x');
ylabel('Density');
hold off;


a = 0.5;
mu = [5;8];
sigma = [1 2*a;2*a 4];
X = normal_gen(Z,mu,sigma,a);
%ques2
figure;
hist3(X',[15 15])
title('Histogram for 0.5')
%simulated
figure;
x=X(1,:);
y=X(2,:);
subplot(2,1,1);
surfc(hist3(X',[10 10])/(1000*((max(x)-min(x))/10)*((max(y)-min(y))/10)))
title('Simulated density for 0.5')
%plotting actual
subplot(2,1,2);
x=X(1,:);
y=X(2,:);
x1 = min(x):.1:max(x); 
x2 = min(y):.1:max(y);
[M1,M2] = meshgrid(x1,x2);
F = mvnpdf([M1(:) M2(:)],mu',sigma);
F = reshape(F,length(x2),length(x1));
surf(x1,x2,F);
% caxis([min(F(:))-.5*range(F(:)),max(F(:))]);
axis([min(x) max(x) min(y) max(y) 0 .15])
xlabel('X1'); ylabel('X2'); zlabel('Probability Density');
title('Actual Density')
%marginal
frange=min(X(1,:)):0.05:max(X(1,:));
range=-20:0.05:20;
rangemid=range/2;
y=(1/(sqrt(2*pi)*sqrt(1)))*exp(-((rangemid-5).*(rangemid-5)/(2*1)));
count=histc(X(1,:),frange);
count=count/(0.05*1000);

figure;
hold on;
plot(frange,count);
title('Marginal Density of x1 for a = 0.5');
plot(rangemid,y,'r','Linewidth',3);
xlabel('Value of x');
ylabel('Density');
hold off;

frange=min(X(2,:)):0.05:max(X(2,:));
range=-20:0.05:30;
rangemid=range/2;
y=(1/(sqrt(2*pi)*sqrt(4)))*exp(-((rangemid-8).*(rangemid-8)/(2*4)));
count=histc(X(2,:),frange);
count=count/(0.05*1000);

figure;
hold on;
plot(frange,count);
title('Marginal Density of x2 for a = 0.5');
plot(rangemid,y,'r','Linewidth',3);
xlabel('Value of x');
ylabel('Density');
hold off;


a = 1;
mu = [5;8];
sigma = [1 2*a;2*a 4];
X = normal_gen(Z,mu,sigma,a);
%ques2
figure;
hist3(X',[15 15])
title('Histogram for a=1')
%simulated
figure;
x=X(1,:);
y=X(2,:);
subplot(2,1,1);
surfc(hist3(X',[10 10])/(1000*((max(x)-min(x))/10)*((max(y)-min(y))/10)))
title('Simulated density for a=1')
%marginal
frange=min(X(1,:)):0.05:max(X(1,:));
range=-20:0.05:20;
rangemid=range/2;
y=(1/(sqrt(2*pi)*sqrt(1)))*exp(-((rangemid-5).*(rangemid-5)/(2*1)));
count=histc(X(1,:),frange);
count=count/(0.05*1000);

figure;
hold on;
plot(frange,count);
title('Marginal Density of x1 for a = 1');
plot(rangemid,y,'r','Linewidth',3);
xlabel('Value of x');
ylabel('Density');
hold off;

frange=min(X(2,:)):0.05:max(X(2,:));
range=-20:0.05:30;
rangemid=range/2;
y=(1/(sqrt(2*pi)*sqrt(4)))*exp(-((rangemid-8).*(rangemid-8)/(2*4)));
count=histc(X(2,:),frange);
count=count/(0.05*1000);

figure;
hold on;
plot(frange,count);
title('Marginal Density of x2 for a = 1');
plot(rangemid,y,'r','Linewidth',3);
xlabel('Value of x');
ylabel('Density');
hold off;

%plotting actual
subplot(2,1,2);
x=X(1,:);
y=X(2,:);
x1 = min(x):.1:max(x); 
x2 = min(y):.1:max(y);
[M1,M2] = meshgrid(x1,x2);
F = mvnpdf([M1(:) M2(:)],mu',sigma);
F = reshape(F,length(x2),length(x1));
surf(x1,x2,F);
% caxis([min(F(:))-.5*range(F(:)),max(F(:))]);
axis([min(x) max(x) min(y) max(y) 0 .15])
xlabel('X1'); ylabel('X2'); zlabel('Probability Density');
title('Actual Density')