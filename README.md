# Online Payment Fraud Detection System Using Machine Learning

## **Project Overview**
The **Online Payment Fraud Detection System** is a Machine Learning based web application that predicts whether an online transaction is **Fraud (1)** or **Safe (0)**.  
The system analyzes transaction details such as step, transaction type, amount, and account balances to identify suspicious activity.

This project combines **Machine Learning** and **Web Development** to provide a simple user interface where users can enter transaction data and instantly receive a fraud prediction.

---

## **Features**
- Detects fraudulent online payment transactions
- Simple and user-friendly web interface
- Real-time prediction using a trained ML model
- Supports transaction types:
  - **PAYMENT**
  - **CASH_OUT**
  - **TRANSFER**
- Displays result as **1 (Fraud)** or **0 (Safe)**

---

## **Technologies Used**
- **Python**
- **Flask**
- **Scikit-Learn**
- **Pandas**
- **NumPy**
- **HTML**
- **CSS**
- **Random Forest Classifier**

---

## **Machine Learning Model**
- **Algorithm:** Random Forest Classifier  
- **Dataset:** Online Payment Fraud Dataset  
- **Output:**  
  - **1 → Fraud Transaction**  
  - **0 → Safe Transaction**

The trained model is saved as a **.pkl file** and loaded in the Flask application for prediction.

---

## **Project Structure**

```
online-payment-fraud-detection/
│
├── app.py
├── model.pkl
│
├── static/
│   └── style.css
│
├── templates/
│   ├── home.html
│   ├── predict.html
│   └── submit.html
│
├── videos/
│   ├── demo.mp4
│   └── code.mp4
│
└── README.md
```
---

## **How to Run the Project**

### **Step 1: Clone Repository**


git clone https://github.com/your-username/online-payment-fraud-detection.git


### **Step 2: Install Dependencies**


pip install flask numpy pandas scikit-learn


### **Step 3: Run Application**


python app.py


### **Step 4: Open in Browser**


http://127.0.0.1:5000


---

## **Input Fields**
- **Step** – Time step of transaction  
- **Type** – Transaction type (0–4)  
- **Amount** – Transaction amount  
- **Old Balance Org** – Sender balance before transaction  
- **New Balance Orig** – Sender balance after transaction  

---

## **Output**
- **1 → Fraud Detected**
- **0 → Safe Transaction**

---

## **Advantages**
- Quick fraud prediction  
- Easy to use interface  
- Lightweight and fast  
- No external APIs required  

---

## **Limitations**
- Depends on dataset accuracy  
- Not connected to real-time banking systems  
- Needs retraining for new fraud patterns  

---

## **Future Scope**
- Integration with real-time payment gateways  
- Mobile application version  
- Advanced Deep Learning models  
- Cloud deployment  

---

## **Demo**
Demo and code explanation videos are available in the **videos** folder.

---

## **Author**
**Ramya Sai Tirumalasetty**
B.Tech – Computer Science & Engineering  

---

## **Acknowledgment**
This project was developed as part of an academic requirement to understand practical applications of **Machine Learning** and **Web Development** in fraud detection systems.

---

## **Conclusion**
This project demonstrates how **Machine Learning** can be used to detect fraudulent online transactions efficiently.  
It provides a strong foundation for building more advanced and real-time fraud detection systems in the future.
