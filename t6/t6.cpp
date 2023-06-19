#include "shortest_path.hpp"

using namespace std;

int main() {

  int n, Q;

  cin >> n;
  cin >> Q;

  int *v = (int *)malloc(n * sizeof(int));
  int *p = (int *)malloc(n * sizeof(int));
  int *q = (int *)malloc(n * sizeof(int));

  for (int i = 0; i < n; i++) {
    cin >> v[i];
    cin >> p[i];
    cin >> q[i];

  }


  Grafo g(n * (Q + 1) + 2);

  g.adicionaArco(0, 1, 0);

  for(int k = 1; k <= q[0]; k++){

      g.adicionaArco(0, k * v[0] + 1, k * p[0]);

  }

  for(int k = 0; k <= Q; k++){

      g.adicionaArco((n - 1) * (Q + 1) + k + 1, n*(Q + 1) + 1, 0);

  }

  for (int i = 2; i <= n; i++) {

    for (int k = 0; k <= Q; k++) {

      for (int j = 0; j <= q[i - 1]; j++) {

        
        int a = (i - 2) * (Q + 1) + k - (j * v[i - 1]) + 1;
        int b = (i - 1) * (Q + 1) + k + 1;
        int c = j * p[i - 1];

        if(j == 0)
          c = 0;

        //printf("a, i, j, k: %d %d %d %d\n", a, i, j, k);

        if(a > 0)
          g.adicionaArco(a, b, c);
        
      }
    }
  }

  int *dist = g.caminhoMinimo(0, n * (Q + 1));

  if(dist[n * (Q + 1)] < INT_MAX){
   
    cout << dist[n * (Q + 1)] << endl;

    free(dist);
    free(v);
    free(p);
    free(q);

    return 0;
  }


  for(int i = n * (Q + 1) - 1; i >= 0; i--){
    
    if(dist[i] < INT_MAX){
   
      cout << i - (n-1)*(Q+1) - 1 << " " << dist[i] << endl;

      free(dist);
      free(v);
      free(p);
      free(q);

      return 0;
    }
  }
}