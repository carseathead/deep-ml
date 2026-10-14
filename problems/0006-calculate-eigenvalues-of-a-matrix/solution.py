import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	trace = matrix[0][0] + matrix[1][1]
	det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

    eigenvalues = []
    discriminant = trace ** 2 - 4 * det
    
    # 2. 근의 공식 부호 수정 및 괄호/콜론(:) 보완
    if discriminant >= 0:
        eigenvalues.append(1/2 * (trace + np.sqrt(discriminant)))
        eigenvalues.append(1/2 * (trace - np.sqrt(discriminant)))

	return eigenvalues