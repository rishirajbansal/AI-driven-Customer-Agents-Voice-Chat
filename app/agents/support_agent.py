from app.chains.retrieval_chain import retrieval_augmented_response

def handle_customer_query(query):
    return retrieval_augmented_response(query)
