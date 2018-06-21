import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	int MAX = 1000005;
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
	
		int casosTeste = scan.nextInt();
		scan.nextLine();

		while (casosTeste > 0) {
			// Lendo input...
			int numRadars = scan.nextInt();
			int distanciaMinima = scan.nextInt();
			scan.nextLine();

			String[] _posicoes = scan.nextLine().split(" ");
			String[] _lucros = scan.nextLine().split(" ");

			// Estrada vai até a posição do último radar
			int ultimaPosicao = Integer.parseInt(_posicoes[_posicoes.length - 1]);

			// Aloca a estrada
			int[] estrada = new int[ultimaPosicao + 1]; // + 1 pois começa de zero
			
			// Preenchendo a estrada
			for (int i = 0; i < numRadars; i++) {
				int posicao = Integer.parseInt(_posicoes[i]);
				int lucro = Integer.parseInt(_lucros[i]);

				estrada[posicao] = Math.max(estrada[posicao], lucro); // Quando os radares têm _mesma_ posição
			}

			// Calculando
			int maiorLucroAteAgora = estrada[0];

			// Começa de 1, assumimos que o maior lucro era o do 0
			for (int km = 1; km <= ultimaPosicao; km++) {
				// Se o poste ainda não tem distância mínima, não posso somá-lo
				// Compara-se, então, com o poste anterior
				if (km < distanciaMinima) {
					maiorLucroAteAgora = Math.max(estrada[km - 1], estrada[km]);
				} else {
					// Opa! Podemos usar algum poste anterior
					// Vamos comparar o KM atual + o KM para trás que atenda a distânciaMinima com o KM anterior
					maiorLucroAteAgora = Math.max(estrada[km - 1], estrada[km] + estrada[km - distanciaMinima]);
				}
				estrada[km] = maiorLucroAteAgora;
			}

			System.out.println(estrada[estrada.length - 1]);

			casosTeste--;
		}
		
	}
}

		/*
		for (int i = 0; i < casosTeste; i++) {
			String linha1 = scan.nextLine();
			
			String[] arrayValores = linha1.split(" ");

			int numRadares = Integer.parseInt(arrayValores[0]);
			int minDistancia = Integer.parseInt(arrayValores[1]);

			int posicaoRadar[] = new int[numRadares + 1];

			String linhaPesos = scan.nextLine();
			
			String[] arrayPesos = linhaPesos.split(" ");

			for (int j = 1; j < numRadares + 1; j++) {
				if (j == 0) {
					posicaoRadar[j] = 0;
				} else {
					posicaoRadar[j] = Integer.parseInt(arrayPesos[j - 1]);
				}
			}
			String linhaValorRadar = scan.nextLine();
			String[] arrayValorRadar = linhaValorRadar.split(" ");

			int lucro[] = new int[numRadares + 1];

			for (int k = 0; k < numRadares + 1; k++) {
				if (k == 0) {
					lucro[k + 1] = 0;
				} else {
					lucro[k] = Integer.parseInt(arrayValorRadar[k - 1]);
				}
			}
			int maxLucro = 0;
			for (int j = 1; j < posicaoRadar.length; j++) {
				if (lucro[j] > maxLucro)
					maxLucro = lucro[j];
			}

			maxRadar = 0;
			for (int j = 1; j < posicaoRadar.length; j++) {
				if (posicaoRadar[j] > maxRadar)
					maxRadar = posicaoRadar[j];
			}

			matriz = new int[2][maxRadar+2];

			if (posicaoRadar.length == 3 && minDistancia == 1) {
				for (int j = 0; j < posicaoRadar.length; j++) {
					matriz[0][j] = posicaoRadar[j];
					matriz[1][j] = lucro[j];
				}
			} else {
				for (int j = 0; j <= maxRadar; j++) {
					for (int j2 = 0; j2 < posicaoRadar.length; j2++) {
						if (posicaoRadar[j2] == j) {
							matriz[0][j] = posicaoRadar[j2];
						}
						if (posicaoRadar[j2] == matriz[0][j]) {
							matriz[1][j] = lucro[j2];
						}
					}
				}
			}

			int maximo = 0;	
			for (int j = 1; j < maxRadar; j++) {
				for (int j2 = 0; j2 <= maxRadar; j2++) {
					if((matriz[0][j2] - minDistancia) >=0 ) {
						if(matriz[1][j2] > maximo) {
							maximo = matriz[1][j2]; 
						}else {
							maximo = matriz[1][j2]+matriz[1][j2-minDistancia];
							matriz[1][j2] = maximo;
						}
						
					}else {
						maximo = Math.max(matriz[1][j2], maximo);
						matriz[1][j2] = maximo;	
					}
					j = j2;
				}
			}
			resultado.add(matriz[1][maxRadar]);
		}
		
		for (int i = 0; i < resultado.size(); i++) {
			System.out.println(resultado.get(i));
		}
		
	}

}
*/