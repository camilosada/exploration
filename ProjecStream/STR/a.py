try:
    import os
    import sys
    import streamlit as st 
    import pandas as pd 
    import matplotlib.pyplot as plt
    from io import BytesIO,StringIO
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import KFold
    from sklearn.model_selection import cross_val_score
    import numpy as np
    from sklearn import metrics
   # print('All Modules Loaded')
except Exception as e:
    print('Some Modules are Missing : {}'.format(e))


STYLE= """
<style>
img{
    max-width: 100%
}
</style>
"""

def read_file():
    """Run this function to display the Streamlit app"""
    #st.info(__doc__)
    #st.markdown(STYLE, unsafe_allow_html=True)
    st.set_option('deprecation.showfileUploaderEncoding', False) # deshabilito un warning
    file = st.file_uploader("Upload file", type = ["csv", "png", "jpg"])
    show_file = st.empty()

    if not file:
        show_file.info('Please Upload a file: {}' .format(' '.join(['csv','png','jpg'])))
        return
    file.getvalue()

    if isinstance(file, BytesIO):
        show_file.image(file)
    else:
        df = pd.read_csv(file)
        df['clase'] = df['class']
    file.close()
    return df

@st.cache
def divide_data(data, percentage):
    colnames = data.columns.values.tolist()
    predictors = colnames[:6]
    target = colnames[7]
    train, test = train_test_split(data, test_size = percentage)
    train = [train[predictors],pd.DataFrame(train[target])]
    test = [test[predictors],pd.DataFrame(test[target])]
    return train,test

 
def tree_method(data,train,test,MaxDepth,MinSamplesSplit,MinSamplesLeaf):
       
    tree = DecisionTreeClassifier(criterion='entropy',max_depth=MaxDepth, min_samples_split= MinSamplesSplit, random_state=99,min_samples_leaf= MinSamplesLeaf) 
    tree.fit(train[0], train[1])
    # una vez el arbol entrenado evaluo el modelo con el data test
    st.write('Model test score')
    st.write(tree.score(test[0], test[1]))
    
    return tree
    

def main():
    data = read_file()

    choice_visualization = st.sidebar.selectbox('Data visualization',['None','Show..'])
    if choice_visualization == 'Show..':
        if st.sidebar.checkbox('Data'):
            st.subheader('Data')
            st.dataframe(data.head(10))
        if st.sidebar.checkbox('Data Shape'):
            st.subheader('Data Shape')
            st.write(data.shape)
        if st.sidebar.checkbox('Output Histogram'):
            st.subheader('Output Histogram')
            plot = data['clase'].value_counts().plot.bar()
            st.pyplot()

             
    if st.sidebar.checkbox('Divide Test/Train', value=False):
        percentage= st.sidebar.slider('Test %',min_value=1,max_value=90)
        train,test = divide_data(data, percentage)
    
    technique = ['None','Tree', 'Forest']
    
    choice_method = st.sidebar.selectbox('Select Technique',technique)
    if choice_method == 'Tree':
        st.subheader('Tree Method')
        MaxDepth= st.sidebar.slider('Max Depth',min_value=1,max_value=90)
        MinSamplesSplit = st.sidebar.slider('Min Samples Split',min_value=2,max_value=90)
        MinSamplesLeaf = st.sidebar.slider('Min Samples Leaf',min_value=1,max_value=90)

        model = tree_method(data,train,test,MaxDepth,MinSamplesSplit,MinSamplesLeaf)
        
        

    elif choice_method == 'Forest':
        st.subheader('Forest Method')

    choice_results = st.sidebar.selectbox('Results visualization',['None','Show..'])
    if choice_results == 'Show..':
        if st.sidebar.checkbox('Mean Cross Validation'):
            st.subheader('Mean Cross Validation')    
            X = (train[0].append(test[0])).sort_index()
            Y = (train[1].append(test[1])).sort_index()
            cv = KFold(n_splits=5, shuffle=True, random_state=1)
            score = np.mean(cross_val_score(model, X,Y, scoring='accuracy',cv=cv,n_jobs=1))
            st.write(score)


main()
