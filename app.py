import gradio as gr
import pickle

def example1():
    
    model = pickle.load(open('model.pkl', 'rb'))
    input_model = [[65,1.8,2,0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1]]
    pred=model.predict(input_model)
    churn = "False"
    if pred[0] == 1:
        churn = "He Will Churn"
    elif pred[0] == 0:
        churn = "He Will Not Churn"
    return churn

def example2():
    
    model = pickle.load(open('model.pkl', 'rb'))
    input_model = [[41,2,2,0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0]]
    pred=model.predict(input_model)
    churn = "False"
    if pred[0] == 1:
        churn = "He Will Churn"
    elif pred[0] == 0:
        churn = "He Will Not Churn"
    return churn


def example3():
    
    model = pickle.load(open('model.pkl', 'rb'))
    input_model = [[10,1.1,2,0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0]]
    pred=model.predict(input_model)
    churn = "False"
    if pred[0] == 1:
        churn = "He Will Churn"
    elif pred[0] == 0:
        churn = "He Will Not Churn"
    return churn

def example4():
    
    model = pickle.load(open('model.pkl', 'rb'))
    input_model = [[7,0.8,5,0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0,0, 0, 1]]
    pred=model.predict(input_model)
    churn = "False"
    if pred[0] == 0:
        churn = "She Will Churn"
    elif pred[0] == 1:
        churn = "She Will Not Churn"
    return churn
    

def greet(Total_Transaction, Total_Ct_Chng_Q4_Q1, Total_Relationship_Count, Education=None, Annual_Income=None, Marital_Status=None, Card_Type=None):
    educ, edud, edug, eduh, edup, eduu, ai0, ai40, ai60, ai80, ai120, msd, msm, mss, ctb, ctg, cts = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    
    if Annual_Income == "0k-40k":
        ai0 = 1
    elif Annual_Income == "40k-60k":
        ai40 = 1
    elif Annual_Income == "60k-80k":
        ai60 = 1
    elif Annual_Income == "80k-120k":
        ai80 = 1
    elif Annual_Income == "120k+":
        ai120 = 1

    if Marital_Status == "Single":
        mss = 1
    elif Marital_Status == "Married":
        msm = 1
    elif Marital_Status == "Divorced":
        msd = 1

    if Card_Type == "Blue":
        ctb = 1
    elif Card_Type == "Gold":
        ctg = 1
    elif Card_Type == "Silver":
        cts = 1

    if Education == "College":
        educ = 1
    elif Education == "Doctorate":
        edud = 1
    elif Education == "Graduate":
        edug = 1
    elif Education == "High-School":
        eduh = 1
    elif Education == "Post-Graduate":
        edup = 1
    elif Education == "Uneducated":
        eduu = 1
        
    
    input_model = [[Total_Transaction,Total_Ct_Chng_Q4_Q1,Total_Relationship_Count,educ, edud, edug, eduh, edup, eduu, ai120, ai40, ai60, ai80, ai0, msd, msm, mss,ctb, ctg, cts]]
    model = pickle.load(open('model.pkl', 'rb'))
    pred=model.predict(input_model)
    churn = "False"
    if pred[0] == 1:
        churn = "True"
    elif pred[0] == 0:
        churn = "Flase"
    return churn
    
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=1,min_width=600):
            gr.Image("logo2.png").style(height='7')
            Total_Transaction = gr.Slider(0, 200,label="Total Transaction Count")
            Total_Ct_Chng_Q4_Q1 = gr.Slider(0, 30,label="Transaction Count Q4 vs Q1")
            Total_Relationship_Count = gr.Slider(0, 20,step=1,label="Total Relationship Count")
            
        with gr.Column(scale=2,min_width=600):
            with gr.Row():
                with gr.Column(scale=1,min_width=300):
                    Annual_Income = gr.Dropdown(["0k-40k","40k-60k","60k-80k","80k-120K","120k+"],label="Annual Income")
                with gr.Column(scale=2,min_width=300):
                    Education = gr.Dropdown(["College","Doctorate","Graduate","High-School","Post-Graduate","Uneducated","Unknown"],label="Education")
                    
            with gr.Row():
                with gr.Column(scale=3,min_width=300):
                    Marital_Status = gr.Dropdown(["Single","Married","Divorced","Unknown"],label="Marital Status")
                with gr.Column(scale=4,min_width=300):
                    Card_Type = gr.Dropdown(["Blue","Silver","Gold"],label="Crad Type")
            churn = gr.Textbox(value="", label="Churn")
            btn = gr.Button("PREDICT").style()
            btn.click(fn=greet, inputs=[Total_Transaction,Total_Ct_Chng_Q4_Q1,Total_Relationship_Count,Education,Annual_Income,Marital_Status,Card_Type], outputs=[churn])
            gr.Markdown("""# Few Examples Based on Real-World Simulations""")
            
    with gr.Row():
        with gr.Column(scale=1,min_width=300):
            gr.Image("avatars/1.png")
            churn1 = gr.Textbox(value="", label="Churn")
            btn1 = gr.Button("PREDICT").style()
            exp =1
            btn1.click(fn=example1, inputs=[], outputs=[churn1])
            gr.Markdown("""
            # Corporate Professional!
            Total Transaction Count - 45\n
            Transaction Count Q4 vs Q1 - 1.3\n
            Total Relationship Count - 2\n
            Annual Income - 40k-60k\n
            Education - Graduate\n
            Marital Status - Married\n
            Card Type - Silver\n
            """)
        with gr.Column(scale=2,min_width=300):
            gr.Image("avatars/4.png")
            churn2 = gr.Textbox(value="", label="Churn")
            bt2 = gr.Button("PREDICT").style()
            bt2.click(fn=example4, inputs=[], outputs=[churn2])
            gr.Markdown("""
            # Medical Professional!
            Total Transaction Count - 7\n
            Transaction Count Q4 vs Q1 - 0.8\n
            Total Relationship Count - 5\n
            Annual Income - 80k-120k\n
            Education - Doctorate\n
            Marital Status - Married\n
            Card Type - Gold\n
            """)
        with gr.Column(scale=3,min_width=300):
            gr.Image("avatars/2.png")
            churn3 = gr.Textbox(value="", label="Churn")
            btn3 = gr.Button("PREDICT").style()
            btn3.click(fn=example2, inputs=[], outputs=[churn3])
            gr.Markdown("""
            # Freelance Photographer!
            Total Transaction Count - 41\n
            Transaction Count Q4 vs Q1 - 2\n
            Total Relationship Count - 2\n
            Annual Income - 0k-40k\n
            Education - High-School\n
            Marital Status - Single\n
            Card Type - Blue\n
            """)
        with gr.Column(scale=4,min_width=300):
            gr.Image("avatars/3.png")
            churn4 = gr.Textbox(value="", label="Churn")
            btn4 = gr.Button("PREDICT").style()
            btn4.click(fn=example3, inputs=[], outputs=[churn4])
            gr.Markdown("""
            # Retired Veteran Pensioner!
            Total Transaction Count - 10\n
            Transaction Count Q4 vs Q1 - 1.1\n
            Total Relationship Count - 2\n
            Annual Income - 80k-120k\n
            Education - Post-Graduate\n
            Marital Status - Divorced\n
            Card Type - GOld\n
            """)

demo.launch()
