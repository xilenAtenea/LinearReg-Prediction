import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import seaborn as sns
import matplotlib.pyplot as plt

def predictions():
    df = pd.read_csv('studentsperformance.csv')

    # Select multiple columns as input variables
    X = df[['math score', 'reading score', 'gender', 'race/ethnicity', 
            'parental level of education', 'lunch', 'test preparation course']]
    Y = df['writing score']

    # One-hot coding for categorical variables
    X = pd.get_dummies(X, columns=['gender', 'race/ethnicity', 'parental level of education', 'lunch', 
                                    'test preparation course'], drop_first=True)

    # Split data for training and testing
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    # Creating and training the model
    reg = LinearRegression()
    reg.fit(X_train, Y_train)

    # Making predictions
    y_pred = reg.predict(X_test)

    # Calculate the mean square error
    meanSquared_error = mean_squared_error(Y_test, y_pred)
    
     # Evaluating the model
    print('Mean square error:', meanSquared_error)
    print('Intercept:', reg.intercept_)
    print('coefficients:')
    for feature, coef in zip(X.columns, reg.coef_):
        print(f'{feature}: {coef}')

    # Scatterplot of actual vs. predicted results with regression line
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=Y_test, y=y_pred, alpha=0.5, color='blue', label='Predictions')
    sns.lineplot(x=Y_test, y=Y_test, color='red', label='Real values')
    plt.title('Actual vs. predicted results')
    plt.xlabel('Real values')
    plt.ylabel('Predictions')
    plt.legend()
    plt.savefig('predictions.png')

    return meanSquared_error, reg, X.columns.tolist()
