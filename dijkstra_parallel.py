import sys
import ast
import multiprocessing as mp
 
INFINITY = 999999
 
def relax(args):
    v, u, distance_dict, visited_dict, graph = args
    if graph[u][v] > 0 and not visited_dict[v]:
        new_dist = distance_dict[u] + graph[u][v]
        if new_dist < distance_dict[v]:
            distance_dict[v] = new_dist
 
def dijkstra_parallel(graph, start):
    num_vertices = len(graph)
 
    with mp.Manager() as manager:
        visited = manager.dict({i: False for i in range(num_vertices)})
        distance = manager.dict({i: INFINITY for i in range(num_vertices)})
        distance[start] = 0
 
        def find_min():
            min_dist = INFINITY
            min_index = -1
            for v in range(num_vertices):
                if not visited[v] and distance[v] < min_dist:
                    min_dist = distance[v]
                    min_index = v
            return min_index
 
        for _ in range(num_vertices):
            u = find_min()
            if u == -1:
                break
            visited[u] = True
 
            args_list = [(v, u, distance, visited, graph) for v in range(num_vertices)]
            with mp.Pool() as pool:
                pool.map(relax, args_list)
 
        return [distance[i] for i in range(num_vertices)]
 
def main():
    try:
        print("Script iniciado con argumentos:", sys.argv)
 
        if len(sys.argv) != 4:
            print("Uso incorrecto: programa \"[[matriz]]\" vertice_inicio archivo_salida")
            print("Argumentos recibidos:", sys.argv)
            sys.exit(1)
 
        graph = ast.literal_eval(sys.argv[1])
        start_vertex = int(sys.argv[2])
        output_file = sys.argv[3]
 
        print("Argumentos OK. Ejecutando algoritmo...")
 
        result = dijkstra_parallel(graph, start_vertex)
 
        with open(output_file, 'w') as f:
            f.write("Vértice\t\tDistancia desde el origen\n")
            for i, dist in enumerate(result):
                f.write(f"{i}\t\t{dist}\n")
 
        print("Resultados escritos en:", output_file)
        print("Resultado final:")
        for i, dist in enumerate(result):
            print(f"{i}\t\t{dist}")
 
    except Exception as e:
        print("Error durante la ejecución:", e)
 
if __name__ == "__main__":
    mp.set_start_method('fork')  
    main()
 