import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables and initialize OpenAI client
load_dotenv()
client = OpenAI(
    base_url = "https://openai.vocareum.com/v1",
    api_key=os.getenv("OPENAI_API_KEY", ""))

# --- Helper Function for API Calls ---
def call_openai(system_prompt, user_prompt, model="gpt-3.5-turbo"):
    """Simple wrapper for OpenAI API calls."""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0
    )
    return response.choices[0].message.content


# --- Agents for Different Retail Tasks ---

def product_researcher_agent(query):
    """Product researcher agent gathers product information."""
    system_prompt = """You are a product research agent for a retail company. Your task is to provide 
    structured information about products, market trends, and competitor pricing."""
    
    user_prompt = f"Research this product thoroughly: {query}"
    return call_openai(system_prompt, user_prompt)


def customer_analyzer_agent(query):
    """Customer analyzer agent processes customer data and feedback."""
    system_prompt = """You are a customer analysis agent. Your task is to analyze customer feedback, 
    preferences, and purchasing patterns."""
    
    user_prompt = f"Analyze customer behavior for: {query}"
    return call_openai(system_prompt, user_prompt)


def pricing_strategist_agent(query, product_data=None, customer_data=None):
    """Pricing strategist agent recommends optimal pricing."""
    system_prompt = """You are a pricing strategist agent. Your task is to recommend optimal pricing 
    strategies based on product research and customer analysis."""
    
    # TODO: Implement this function
    user_prompt = f"""
    product info: {product_data or ""}
    ------------
    customer analysis: {customer_data or ""} 
    """
    # It should use product_data and customer_data to inform the pricing strategy
    return call_openai(
        system_prompt,
        user_prompt,
    )


# --- Routing Agent with LLM-Based Task Determination ---
def routing_agent(query, *args):
    """Routing agent that determines which agent to use based on the query."""
    
    # TODO: Implement the routing agent
    # 1. Use an LLM to analyze the query and determine the correct task type
    # 2. Route the query to the appropriate agent
    # 3. Return the results from the chosen agent
    system_prompt = """You are a helpful AI assistant that categorizes retail-related user queries. Based on the user's query, determine if it is primarily about:
        * "product research" (e.g., asking for product specs, trends, competitor prices)
        * "customer analysis" (e.g., asking about customer feedback, preferences, purchase patterns)
        * "pricing strategy" (e.g., asking for optimal pricing for a product)
        Respond only with one of these exact phrases: "product research", "customer analysis", or "pricing strategy".
    """
    user_prompt = f"query: {query}"
    return call_openai(
        system_prompt,
        user_prompt,
    )


# --- Example Usage ---
if __name__ == "__main__":
    # Example queries
    queries = [
        "What are the specifications and current market trends for wireless earbuds?",
        "What do customers think about our premium coffee brand?",
        "What should be the optimal price for our new organic skincare line?"
    ]
    
    # Process each query
    for query in queries:
        print(f"\nQuery: {query}")
        print("\nProcessing...")
        
        # TODO: Use the routing agent to process the query
        task_type = routing_agent(query).replace("\"", "")
        product_context_query = query
        customer_context_query = query
        if task_type == "product research":
            print("  -> Calling Product Researcher Agent...")
            product_info = product_researcher_agent(product_context_query)
            continue
        elif task_type == "customer analysis":
            print("  -> Calling Customer Analyzer Agent...")
            customer_info = customer_analyzer_agent(customer_context_query)
            continue
        elif task_type == "pricing strategy":
            print("  -> Calling Pricing Strategist Agent with gathered data...")
            print(pricing_strategist_agent(query, product_info, customer_info))
        else:
            print("Unknow Type of task", task_type)