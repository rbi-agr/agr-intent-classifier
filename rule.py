from collections import Counter, defaultdict

def create_keyword_mapping():
    usecase_keywords = [
       ("CHEQUE_BOOK", [
           "Cheque", "Check", "Cheque book", "Check book", "book",
           "Cheque leaf", "Cheque leaves", "Cheque delivery", "Check delivery",
           "Status of cheque book", "Cheque status", "Check status",
           "New cheque book", "Order cheque book", "Request cheque book",
           "Cheque book order", "Cheque book request", "Cheque dispatch",
           "Cheque not received", "Cheque book delay", "Cheque book request status",
           "Cheque book replacement", "Cheque reissue"
           ]),
       ("NEFT", [
           "NEFT", "Transfer", "account", "Money transfer", "UTR", "UTR number",
           "Transfer enquiry", "Transaction status", "Amount transfer",
           "Amt transfer", "Paise transfer", "Rupees transfer",
           "Transfer status", "National electronic funds transfer",
           "funds transfer", "fund/ funds", "NEFT status", "NEFT tracking",
           "Bank transfer", "Wire transfer", "NEFT delay", "NEFT timing",
           "NEFT receipt", "NEFT confirmation", "NEFT processing"
       ]),
       ("RTGS", [
           "RTGS", "Real time Gross settlement", "account", "Money transfer",
           "Instant money transfer", "transfer", "UTR", "UTR enquiry",
           "UTR number", "Money transfer", "Paise transfer",
           "Funds/ fund transfer", "RTGS status", "RTGS tracking",
           "RTGS transaction", "RTGS confirmation", "RTGS fee",
           "RTGS delay", "RTGS cutoff", "RTGS time", "RTGS processing",
           "RTGS receipt"
       ]),
       ("LOAN_ENQUIRY", [
           "Loan", "Balance", "account", "Outstanding balance", "Balance enquiry",
           "Balance status", "Loan Amount outstanding", "Loan amount",
           "Loan balance transaction", "Loan payment", "Loan interest",
           "Loan rate", "Loan status", "Loan application",
           "Loan repayment", "Loan schedule", "EMI", "Loan tenure",
           "Loan due date", "Loan overdue", "Loan delay", "Loan restructuring",
           "Loan foreclosure", "Loan prepayment", "Loan EMI calculator"
       ])

       ]

    keyword_mapping = defaultdict(list)
    for usecase, keywords in usecase_keywords:
        if usecase in ["CHEQUE_BOOK", "NEFT", "RTGS", "LOAN_ENQUIRY"]:
            for keyword in keywords:
                keyword_mapping[keyword].append(usecase)
    return keyword_mapping

keyword_mapping = create_keyword_mapping()

def calculate_probabilities_usecase(query):
    usecase_counts = Counter()
    for keyword, usecases in keyword_mapping.items():
        if keyword.lower() in query.lower():
            # print(keyword)
            for usecase in usecases:
                usecase_counts[usecase] += 1
    if usecase_counts:
        max_probability_usecase = max(usecase_counts, key=usecase_counts.get)
        return { "useCase": max_probability_usecase }
    else:
        return { "useCase": 'Other' }
