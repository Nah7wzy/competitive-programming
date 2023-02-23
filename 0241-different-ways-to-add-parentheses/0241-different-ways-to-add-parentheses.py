class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Check if the expression is a single number
        if expression.isdigit():
            return [int(expression)]

        result = []
        # Iterate through each character in the expression
        for i in range(len(expression)):
            # Check if the character is an operator
            if expression[i] in "+-*":
                # Split the expression into two parts and recursively compute the results for each part
                left_results = self.diffWaysToCompute(expression[:i])
                right_results = self.diffWaysToCompute(expression[i+1:])
                # Combine the results for each part using the operator
                for left in left_results:
                    for right in right_results:
                        if expression[i] == "+":
                            result.append(left + right)
                        elif expression[i] == "-":
                            result.append(left - right)
                        elif expression[i] == "*":
                            result.append(left * right)
        return result
