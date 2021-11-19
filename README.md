# MCOC2021-P3-Grupo-07

# N° de grupo : 07
# Integrantes :
              Matías Etcheverry
              Anibal Rodriguez
              David Sanguinetti
![image](https://user-images.githubusercontent.com/88542346/141038925-586ff449-bac2-474f-b57e-490e9910265e.png)

![image](https://user-images.githubusercontent.com/88542346/141038974-c6a896e6-15bd-4696-800a-ae95300de894.png)

![image](https://user-images.githubusercontent.com/88542346/141039013-793f12a1-6b26-4c6c-b5ba-58730ef3d766.png)

![image](https://user-images.githubusercontent.com/88542346/141039031-c2d040a6-80a0-4a4b-a12d-2b925c36602d.png)

# ENTREGA 3

  David Sanguinetti Olivares
  
  Zona de domicilio : 159 , Comuna de Independencia.
  
![image](https://user-images.githubusercontent.com/88542346/141600501-545ab65f-529f-4cf9-9742-b0d55b9a3af4.png)

-
-
-
-
Aníbal Rodríguez Molina

![image](https://user-images.githubusercontent.com/88512479/141602007-7d9e6edd-19ec-49ca-8057-d0819896cd71.png)

-
-
-
-
Matias Etcheverry Fuentealba

![image](https://github.com/meetcheverry/MCOC2021-P3-Grupo-07/blob/main/Figure%202021-11-12%20231824.png)


# ENTREGA 4

* Grafico a resolver
 ![image](https://user-images.githubusercontent.com/88542346/142120109-e9c92e95-425d-4dcf-bb05-5c65391e9dd6.png)

* Costos de las rutas
![image](https://user-images.githubusercontent.com/88542346/142120538-e24605b7-7a55-4fc9-a128-c87a9c5a68b1.png)

* Flujos de las rutas
![image](https://user-images.githubusercontent.com/88542346/142121087-9d498b38-b31d-4616-a32d-8365d0512003.png)

 *ANALISIS DEL CODIGO*
 ![image](https://user-images.githubusercontent.com/88542346/142121962-7d777d7a-cc0d-482a-94cc-f9b6b1f5e85c.png)
 
  Primero se definieron nodos y arcos
  
  ![image](https://user-images.githubusercontent.com/88542346/142122798-da6fa2bd-e490-439a-86c9-196995147229.png)
  
  Primero es necesario tener una copia de la matriz para su comparación(demanda)
  
  Luego en las siguientes  estas lineas se divide la demanda de bloques de un 10% y el incremento del 0,1% en cada una de ellas, al encontrar la satisfación con un flujo mejor, actualzia la variable y la deja enla matriz.
  
  Respecto al punto anterior se encontraron discrepancias en el gráfico con la solución expresada, posiblementes a acotamientos del gráfico o falla en la comprobación de iteraciones





-
-
-
-


# ENTREGA 5

Grafo :
    
   ![image](https://user-images.githubusercontent.com/88542346/142703356-36e8095e-00ee-45e4-877d-0add0c34284a.png)





¿Como selecciono las zonas a incluir?



Los zonas las seleccionamos segun los siguientes criterios:

-  Primero tratamos de hacer una función en Python la cual recorriera la lista de origenes y destinos y poder ir seleccionando cuales nos servian con respecto a algunos criterios, pero no lo pudimos completar de manera correcta ya que nos tiraba error. Es por esto que decidimos hacerlo de una forma segura pero muy larga, ir viendo uno por uno en la pagina http://datos.cedeus.cl/layers/geonode:eod2012_utm19s, que las zonas (Origen y Destino) tengan setido que pasen por AVO (Americo Vespucio Oriente). Por lo que fue un arduo trabajo viendo uno por uno los casi 3 mil datos de origen destino, para ir eliminando las zonas las cuales no tenian sentido que pasen por AVO. 

- También intentamos implementar un ciclo for para recorrer los arcos (Edges) y retirar de la Matriz OD cada par origen-destino que haciendo la ruta mínima pasara por edges con "name" "Americo Vespucio Oriente" or "Avenida Ossa" ,pero debido a un errores de lectura en la lista en la función G.edges.remove.from() , optamos por trabajar la matriz dictada por el primer método antes nombrado.
- ![image](https://user-images.githubusercontent.com/88542346/142702598-3d21652e-2371-4362-bebb-bc3737bc4d4f.png)

