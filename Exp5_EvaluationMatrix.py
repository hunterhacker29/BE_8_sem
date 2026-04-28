# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# # load dataset
# df = pd.read_csv("VizStudentData.csv")

# # features (input)
# X = df[["math_marks", "science_marks", "english_marks", "attendance"]]

# # target (output)
# y = df["department"]

# # split data
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# # create model
# model = DecisionTreeClassifier()

# # train model
# model.fit(X_train, y_train)

# # prediction
# y_pred = model.predict(X_test)

# # ---------------------------
# # Evaluation
# # ---------------------------

# # Confusion Matrix
# cm = confusion_matrix(y_test, y_pred)
# print("Confusion Matrix:\n", cm)

# # Accuracy
# acc = accuracy_score(y_test, y_pred)
# print("\nAccuracy:", acc)

# # Classification Report
# print("\nClassification Report:\n")
# print(classification_report(y_test, y_pred))




import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.metrics import confusion_matrix , accuracy_score , classification_report 
from sklearn.tree import DecisionTreeClassifier


df = pd.DataFrame(
    
    {
        "math_marks":[60, 70, 80, 90, 75],
        "science_marks":[65, 75, 85, 95, 70],
        "english_marks":[55, 65, 75, 85, 60],
        "attendance":[80, 90, 95, 100, 85],
        "department":["A", "B", "A", "B", "A"]
    }
)



print(df)


x= df[["math_marks", "science_marks", "english_marks", "attendance"]]
y = df["department"]
x_train , x_test , y_train , y_test = train_test_split(x,y) 

model  = DecisionTreeClassifier()

model.fit(x_train , y_train)

y_pred = model.predict(x_test)
print(f"Model Accuracy : {accuracy_score(y_test,y_pred)}")
print(f"Confusion Matrix : \n {confusion_matrix(y_test,y_pred)}")
print(f"Classification Report : \n {classification_report(y_test,y_pred)}")