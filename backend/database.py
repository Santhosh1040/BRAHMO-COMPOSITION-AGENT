import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)


def get_candidate_nodes():
    response = (
        supabase
        .table("candidate_nodes")
        .select("*")
        .execute()
    )

    return response.data 
def get_patients():

    response = (
        supabase.table("patients")
        .select("*")
        .execute()
    )

    return response.data


def get_patient(patient_id):

    response = (
        supabase.table("patients")
        .select("*")
        .eq("id", patient_id)
        .execute()
    )

    return response.data


def get_users():

    response = (
        supabase.table("users")
        .select("*")
        .execute()
    )

    return response.data