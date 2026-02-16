from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def cluster_comments(cleaned_comments, num_clusters=5, top_n=10):
    """
    Input:
        cleaned_comments : قائمة التعليقات بعد المعالجة
        num_clusters : عدد الـ clusters
        top_n : عدد الكلمات الأساسية لكل cluster
    Output:
        labels : قائمة تسميات كل تعليق
        cluster_top_words : قائمة كلمات لكل cluster
    """
    vectorizer = TfidfVectorizer(max_features=500, stop_words=None)
    X = vectorizer.fit_transform(cleaned_comments)
    
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(X)
    
    labels = kmeans.labels_
    
    terms = vectorizer.get_feature_names_out()
    cluster_top_words = []
    
    for i in range(num_clusters):
        centroid = kmeans.cluster_centers_[i]
        top_indices = centroid.argsort()[-top_n:][::-1]
        top_words = [terms[ind] for ind in top_indices]
        cluster_top_words.append(top_words)
    
    return labels, cluster_top_words
