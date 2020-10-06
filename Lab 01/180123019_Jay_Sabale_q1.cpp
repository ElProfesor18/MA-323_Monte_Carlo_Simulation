#include <bits/stdc++.h>

using namespace std;
typedef long long int ll;

void solve(ll a, ll b, ll m, ll x0){
	ll xi = x0;

	cout<<x0<<"\t";
	for(int i=1; i<=10; i++){
		ll xii = (a*xi + b) % m;
		cout<<xii<<"\t";
		xi = xii;
	} cout<<"\n";
}

int main(){

	cout<<"Case I:\n";
	ll a=6, b=0, m=11;
	for(int i=0; i<=10; i++){
		cout<<i<<"\t";
	}cout<<"\n";

	for(ll x0=0; x0<=10; x0++){
		solve(a, b, m, x0);
	}cout<<"\n\n\n";

	cout<<"Case II:\n";
	a=3, b=0, m=11;
	for(int i=0; i<=10; i++){
		cout<<i<<"\t";
	}cout<<"\n";

	for(ll x0=0; x0<=10; x0++){
		solve(a, b, m, x0);
	}

	return 0;
}