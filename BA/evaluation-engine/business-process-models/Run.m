clear
clc
x1 = webread("http://localhost:8080/w1");
S1 = x1.AverageServiceTime;
x2 = webread("http://localhost:8080/w2");
S2 = x2.AverageServiceTime;
x3 = webread("http://localhost:8080/w3");
S3 = x3.AverageServiceTime;

% for test:
%S1 = 1;
%S2= 2;
%S3=3;

sim('CaseStudy_Simulink');


