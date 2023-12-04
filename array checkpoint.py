#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def calculate_grades(scores):
    # Define the grade boundaries and corresponding grades
    grade_boundaries = [90, 80, 70, 60, 0]
    grades = ['A', 'B', 'C', 'D', 'F']

    # Use numpy's digitize function to find the appropriate grade for each score
    grade_indices = np.digitize(scores, bins=grade_boundaries, right=True)

    # Map the grade indices to actual grades
    final_grades = [grades[i-1] for i in grade_indices]

    return final_grades

def main():
    # Example scores as a NumPy array
    student_scores = np.array([85, 92, 78, 60, 45, 70, 88])

    # Calculate grades using the defined function
    grades = calculate_grades(student_scores)

    # Print the results
    for i in range(len(student_scores)):
        print(f"Student {i+1}: Score = {student_scores[i]}, Grade = {grades[i]}")

if __name__ == "__main__":
    main()


# In[ ]:




