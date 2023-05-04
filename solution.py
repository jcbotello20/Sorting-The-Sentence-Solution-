class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()  # separar la cadena en palabras
        result = [""] * len(words)  # lista vacía para almacenar las palabras en el orden correcto
        
        for word in words:
            index = int(word[-1]) - 1  # extraer el número final y calcular el índice
            result[index] = word[:-1]  # agregar la palabra en la posición correcta
        
        return " ".join(result)  # unir las palabras para formar la cadena de salida
