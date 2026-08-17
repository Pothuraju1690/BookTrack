import streamlit as st
import pandas as pd
import os
import textwrap


# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="BookTrack",
    page_icon="📚",
    layout="wide"
)


# ============================================================
# Custom Styling
# ============================================================

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #0f1117;
    }

    /* Remove extra top space */
    .block-container {
    padding-top: 3rem;
    padding-bottom: 2rem;
}

    /* Main title */
    .main-title {
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .sub-title {
        color: #9ca3af;
        font-size: 15px;
        margin-bottom: 25px;
    }

    /* Dashboard cards */
    .dashboard-card {
        background-color: #181b24;
        border: 1px solid #292d38;
        border-radius: 12px;
        padding: 20px;
        min-height: 125px;
    }

    .card-icon {
        font-size: 25px;
    }

    .card-title {
        color: #9ca3af;
        font-size: 14px;
        margin-top: 8px;
    }

    .card-value {
        font-size: 30px;
        font-weight: 700;
        margin-top: 3px;
    }

    /* Section cards */
    .section-box {
        background-color: #181b24;
        border: 1px solid #292d38;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #151820;
        border-right: 1px solid #292d38;
    }

    /* Sidebar buttons */
    section[data-testid="stSidebar"] button {
        border-radius: 8px;
    }

    /* Hide default sidebar collapse control */
    button[data-testid="stBaseButton-headerNoPadding"] {
        display: none;
    }

    /* Status badges */
    .available {
        color: #22c55e;
        font-weight: 600;
    }

    .issued {
        color: #f59e0b;
        font-weight: 600;
    }

    /* Quick action buttons */
    .quick-title {
        font-size: 22px;
        font-weight: 600;
        margin-bottom: 15px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #6b7280;
        font-size: 13px;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 1px solid #292d38;
    }

    .top-navigation {
    display: flex;
    align-items: center;
    min-height: 45px;
    margin-bottom: 10px;
}

.top-brand {
    font-size: 32px;
    font-weight: 700;
    line-height: 1.2;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# Classes
# ============================================================

class Book:

    def __init__(self, book_id, name, author, category, price):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.category = category
        self.price = price
        self.status = "Available"

    def display(self):
        print(self.name)


class Member:

    def __init__(self, member_id, name, phone, email):
        self.member_id = member_id
        self.name = name
        self.phone = phone
        self.email = email

    def display(self):
        print(self.name)


# ============================================================
# Load Data
# ============================================================

def load_books():

    if os.path.exists("books.csv"):

        return pd.read_csv(
            "books.csv",
            dtype={
                "Book ID": str,
                "Book Name": str,
                "Author": str,
                "Category": str,
                "Status": str
            }
        )

    return pd.DataFrame(
        columns=[
            "Book ID",
            "Book Name",
            "Author",
            "Category",
            "Price",
            "Status"
        ]
    )


def load_members():

    if os.path.exists("members.csv"):

        return pd.read_csv(
            "members.csv",
            dtype={
                "Member ID": str,
                "Name": str,
                "Phone": str,
                "Email": str
            }
        )

    return pd.DataFrame(
        columns=[
            "Member ID",
            "Name",
            "Phone",
            "Email"
        ]
    )


def load_issues():

    if (
        os.path.exists("issues.csv")
        and os.path.getsize("issues.csv") > 0
    ):

        return pd.read_csv(
            "issues.csv",
            dtype={
                "Issue ID": str,
                "Book ID": str,
                "Member ID": str,
                "Issue Date": str,
                "Status": str
            }
        )

    return pd.DataFrame(
        columns=[
            "Issue ID",
            "Book ID",
            "Member ID",
            "Issue Date",
            "Status"
        ]
    )


# ============================================================
# Session State
# ============================================================

if "sidebar_open" not in st.session_state:

    st.session_state.sidebar_open = True


if "page" not in st.session_state:

    st.session_state.page = "Dashboard"


# ============================================================
# Sidebar Toggle + Top Header
# ============================================================

top_col1, top_col2 = st.columns([0.07, 0.93])

with top_col1:

    if st.button(
        "☰",
        key="menu_button",
        help="Open / Close Sidebar"
    ):
        st.session_state.sidebar_open = (
            not st.session_state.sidebar_open
        )

        st.rerun()


with top_col2:

    st.markdown(
        """
        <div class="top-brand">
            📚 BookTrack
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# Sidebar
# ============================================================

if st.session_state.sidebar_open:

    with st.sidebar:

        st.markdown(
            """
            <div style="
                font-size:26px;
                font-weight:700;
                margin-bottom:5px;
            ">
                📚 BookTrack
            </div>

            <div style="
                color:#9ca3af;
                font-size:13px;
                margin-bottom:25px;
            ">
                Library Management System
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("### Navigation")

        if st.button(
            "🏠  Dashboard",
            use_container_width=True
        ):

            st.session_state.page = "Dashboard"
            st.rerun()


        if st.button(
            "📚  Books",
            use_container_width=True
        ):

            st.session_state.page = "Books"
            st.rerun()


        if st.button(
            "👥  Members",
            use_container_width=True
        ):

            st.session_state.page = "Members"
            st.rerun()


        if st.button(
            "🔄  Circulation",
            use_container_width=True
        ):

            st.session_state.page = "Circulation"
            st.rerun()


        if st.button(
            "📊  Reports",
            use_container_width=True
        ):

            st.session_state.page = "Reports"
            st.rerun()


        st.markdown("---")

        st.caption("BookTrack")
        st.caption("Library Management System")


# ============================================================
# Load Current Data
# ============================================================

books_df = load_books()
members_df = load_members()
issues_df = load_issues()


# ============================================================
# DASHBOARD
# ============================================================

if st.session_state.page == "Dashboard":

    st.markdown(
        '<div class="main-title">📊 Dashboard</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">'
        'Welcome to BookTrack Library Management System'
        '</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # Statistics
    # --------------------------------------------------------

    total_books = len(books_df)

    total_members = len(members_df)

    available_books = len(
        books_df[
            books_df["Status"] == "Available"
        ]
    )

    issued_books = len(
        books_df[
            books_df["Status"] == "Issued"
        ]
    )


    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
        textwrap.dedent(f"""
        <div class="dashboard-card">
            <div class="card-icon">📚</div>
            <div class="card-title">Total Books</div>
            <div class="card-value">{total_books}</div>
        </div>
        """),
        unsafe_allow_html=True
    )

    with col2:
        st.markdown(
        textwrap.dedent(f"""
        <div class="dashboard-card">
            <div class="card-icon">👥</div>
            <div class="card-title">Total Members</div>
            <div class="card-value">{total_members}</div>
        </div>
        """),
        unsafe_allow_html=True
    )

    with col3:
        st.markdown(
        textwrap.dedent(f"""
        <div class="dashboard-card">
            <div class="card-icon">✅</div>
            <div class="card-title">Available Books</div>
            <div class="card-value">{available_books}</div>
        </div>
        """),
        unsafe_allow_html=True
    )

    with col4:
        st.markdown(
        textwrap.dedent(f"""
        <div class="dashboard-card">
            <div class="card-icon">📕</div>
            <div class="card-title">Issued Books</div>
            <div class="card-value">{issued_books}</div>
        </div>
        """),
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # Quick Actions
    # --------------------------------------------------------

    st.markdown(
        '<div class="quick-title">⚡ Quick Actions</div>',
        unsafe_allow_html=True
    )


    q1, q2, q3, q4 = st.columns(4)


    with q1:

        if st.button(
            "➕ Add Book",
            use_container_width=True
        ):

            st.session_state.page = "Books"
            st.session_state.book_action = "Add Book"
            st.rerun()


    with q2:

        if st.button(
            "👤 Add Member",
            use_container_width=True
        ):

            st.session_state.page = "Members"
            st.session_state.member_action = "Add Member"
            st.rerun()


    with q3:

        if st.button(
            "📕 Issue Book",
            use_container_width=True
        ):

            st.session_state.page = "Circulation"
            st.session_state.circulation_action = "Issue Book"
            st.rerun()


    with q4:

        if st.button(
            "🔄 Return Book",
            use_container_width=True
        ):

            st.session_state.page = "Circulation"
            st.session_state.circulation_action = "Return Book"
            st.rerun()


    # --------------------------------------------------------
    # Recent Books
    # --------------------------------------------------------

    st.write("")

    st.subheader("📚 Recent Books")

    if len(books_df) > 0:

        st.dataframe(
            books_df.tail(5),
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No books have been added yet."
        )


# ============================================================
# BOOKS
# ============================================================

elif st.session_state.page == "Books":

    st.markdown(
        '<div class="main-title">📚 Books</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">'
        'Manage your library books'
        '</div>',
        unsafe_allow_html=True
    )


    book_action = st.radio(
        "Book Management",
        [
            "Add Book",
            "View / Search",
            "Update Book",
            "Delete Book"
        ],
        horizontal=True
    )


    # --------------------------------------------------------
    # Add Book
    # --------------------------------------------------------

    if book_action == "Add Book":

        st.subheader("➕ Add New Book")

        col1, col2 = st.columns(2)

        with col1:

            book_id = st.text_input(
                "Book ID"
            )

            book_name = st.text_input(
                "Book Name"
            )

            author = st.text_input(
                "Author"
            )

        with col2:

            category = st.text_input(
                "Category"
            )

            price = st.number_input(
                "Price",
                min_value=0.0
            )


        if st.button(
            "➕ Add Book",
            type="primary"
        ):

            if book_id == "":

                st.error(
                    "Book ID cannot be empty."
                )

            elif book_name == "":

                st.error(
                    "Book Name cannot be empty."
                )

            elif book_id in books_df["Book ID"].values:

                st.error(
                    "Book ID already exists."
                )

            else:

                book = Book(
                    book_id,
                    book_name,
                    author,
                    category,
                    price
                )

                new_book = {
                    "Book ID": book.book_id,
                    "Book Name": book.name,
                    "Author": book.author,
                    "Category": book.category,
                    "Price": book.price,
                    "Status": book.status
                }

                books_df = pd.concat(
                    [
                        books_df,
                        pd.DataFrame([new_book])
                    ],
                    ignore_index=True
                )

                books_df.to_csv(
                    "books.csv",
                    index=False
                )

                st.success(
                    "✅ Book added successfully!"
                )


    # --------------------------------------------------------
    # View / Search Books
    # --------------------------------------------------------

    elif book_action == "View / Search":

        st.subheader("🔍 Search Books")

        search = st.text_input(
            "Search by Book ID, Name, Author or Category"
        )


        if search:

            result = books_df[
                books_df["Book ID"].str.contains(
                    search,
                    case=False,
                    na=False
                )
                |
                books_df["Book Name"].str.contains(
                    search,
                    case=False,
                    na=False
                )
                |
                books_df["Author"].str.contains(
                    search,
                    case=False,
                    na=False
                )
                |
                books_df["Category"].str.contains(
                    search,
                    case=False,
                    na=False
                )
            ]

        else:

            result = books_df


        st.dataframe(
            result,
            use_container_width=True,
            hide_index=True
        )


    # --------------------------------------------------------
    # Update Book
    # --------------------------------------------------------

    elif book_action == "Update Book":

        st.subheader("✏️ Update Book")

        update_id = st.text_input(
            "Book ID to update"
        )

        col1, col2 = st.columns(2)

        with col1:

            new_name = st.text_input(
                "New Book Name"
            )

            new_author = st.text_input(
                "New Author"
            )

        with col2:

            new_category = st.text_input(
                "New Category"
            )

            new_price = st.number_input(
                "New Price",
                min_value=0.0
            )


        if st.button(
            "✏️ Update Book",
            type="primary"
        ):

            if update_id in books_df["Book ID"].values:

                books_df.loc[
                    books_df["Book ID"] == update_id,
                    "Book Name"
                ] = new_name

                books_df.loc[
                    books_df["Book ID"] == update_id,
                    "Author"
                ] = new_author

                books_df.loc[
                    books_df["Book ID"] == update_id,
                    "Category"
                ] = new_category

                books_df.loc[
                    books_df["Book ID"] == update_id,
                    "Price"
                ] = new_price

                books_df.to_csv(
                    "books.csv",
                    index=False
                )

                st.success(
                    "✅ Book updated successfully!"
                )

            else:

                st.error(
                    "Book ID not found."
                )


    # --------------------------------------------------------
    # Delete Book
    # --------------------------------------------------------

    elif book_action == "Delete Book":

        st.subheader("🗑️ Delete Book")

        delete_id = st.text_input(
            "Book ID to delete"
        )


        if st.button(
            "🗑️ Delete Book",
            type="primary"
        ):

            if delete_id in books_df["Book ID"].values:

                status = books_df.loc[
                    books_df["Book ID"] == delete_id,
                    "Status"
                ].values[0]


                if status == "Issued":

                    st.warning(
                        "⚠️ This book cannot be deleted "
                        "because it is currently issued."
                    )

                else:

                    books_df = books_df[
                        books_df["Book ID"] != delete_id
                    ]

                    books_df.to_csv(
                        "books.csv",
                        index=False
                    )

                    st.success(
                        "✅ Book deleted successfully!"
                    )

            else:

                st.error(
                    "Book ID not found."
                )


# ============================================================
# MEMBERS
# ============================================================

elif st.session_state.page == "Members":

    st.markdown(
        '<div class="main-title">👥 Members</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">'
        'Manage library members'
        '</div>',
        unsafe_allow_html=True
    )


    member_action = st.radio(
        "Member Management",
        [
            "Add Member",
            "View / Search",
            "Update Member",
            "Delete Member"
        ],
        horizontal=True
    )


    # --------------------------------------------------------
    # Add Member
    # --------------------------------------------------------

    if member_action == "Add Member":

        st.subheader("➕ Add New Member")

        col1, col2 = st.columns(2)

        with col1:

            member_id = st.text_input(
                "Member ID"
            )

            member_name = st.text_input(
                "Name"
            )

        with col2:

            phone = st.text_input(
                "Phone"
            )

            email = st.text_input(
                "Email"
            )


        if st.button(
            "➕ Add Member",
            type="primary"
        ):

            if member_id == "":

                st.error(
                    "Member ID cannot be empty."
                )

            elif member_name == "":

                st.error(
                    "Name cannot be empty."
                )

            elif member_id in members_df["Member ID"].values:

                st.error(
                    "Member ID already exists."
                )

            else:

                member = Member(
                    member_id,
                    member_name,
                    phone,
                    email
                )

                new_member = {
                    "Member ID": member.member_id,
                    "Name": member.name,
                    "Phone": member.phone,
                    "Email": member.email
                }

                members_df = pd.concat(
                    [
                        members_df,
                        pd.DataFrame([new_member])
                    ],
                    ignore_index=True
                )

                members_df.to_csv(
                    "members.csv",
                    index=False
                )

                st.success(
                    "✅ Member added successfully!"
                )


    # --------------------------------------------------------
    # View / Search Members
    # --------------------------------------------------------

    elif member_action == "View / Search":

        st.subheader("🔍 Search Members")

        search = st.text_input(
            "Search by Member ID, Name or Phone"
        )


        if search:

            result = members_df[
                members_df["Member ID"].str.contains(
                    search,
                    case=False,
                    na=False
                )
                |
                members_df["Name"].str.contains(
                    search,
                    case=False,
                    na=False
                )
                |
                members_df["Phone"].str.contains(
                    search,
                    case=False,
                    na=False
                )
            ]

        else:

            result = members_df


        st.dataframe(
            result,
            use_container_width=True,
            hide_index=True
        )


    # --------------------------------------------------------
    # Update Member
    # --------------------------------------------------------

    elif member_action == "Update Member":

        st.subheader("✏️ Update Member")

        update_id = st.text_input(
            "Member ID to update"
        )

        col1, col2 = st.columns(2)

        with col1:

            new_name = st.text_input(
                "New Name"
            )

            new_phone = st.text_input(
                "New Phone"
            )

        with col2:

            new_email = st.text_input(
                "New Email"
            )


        if st.button(
            "✏️ Update Member",
            type="primary"
        ):

            if update_id in members_df["Member ID"].values:

                members_df.loc[
                    members_df["Member ID"] == update_id,
                    "Name"
                ] = new_name

                members_df.loc[
                    members_df["Member ID"] == update_id,
                    "Phone"
                ] = new_phone

                members_df.loc[
                    members_df["Member ID"] == update_id,
                    "Email"
                ] = new_email

                members_df.to_csv(
                    "members.csv",
                    index=False
                )

                st.success(
                    "✅ Member updated successfully!"
                )

            else:

                st.error(
                    "Member ID not found."
                )


    # --------------------------------------------------------
    # Delete Member
    # --------------------------------------------------------

    elif member_action == "Delete Member":

        st.subheader("🗑️ Delete Member")

        delete_id = st.text_input(
            "Member ID to delete"
        )


        if st.button(
            "🗑️ Delete Member",
            type="primary"
        ):

            if delete_id in members_df["Member ID"].values:

                active_issue = False


                if len(issues_df) > 0:

                    active_issue = (
                        (issues_df["Member ID"] == delete_id)
                        &
                        (issues_df["Status"] == "Issued")
                    ).any()


                if active_issue:

                    st.warning(
                        "⚠️ This member cannot be deleted "
                        "because they have an issued book."
                    )

                else:

                    members_df = members_df[
                        members_df["Member ID"] != delete_id
                    ]

                    members_df.to_csv(
                        "members.csv",
                        index=False
                    )

                    st.success(
                        "✅ Member deleted successfully!"
                    )

            else:

                st.error(
                    "Member ID not found."
                )


# ============================================================
# CIRCULATION
# ============================================================

elif st.session_state.page == "Circulation":

    st.markdown(
        '<div class="main-title">🔄 Circulation</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">'
        'Issue and return library books'
        '</div>',
        unsafe_allow_html=True
    )


    circulation_action = st.radio(
        "Circulation",
        [
            "Issue Book",
            "Return Book"
        ],
        horizontal=True
    )


    # --------------------------------------------------------
    # Issue Book
    # --------------------------------------------------------

    if circulation_action == "Issue Book":

        st.subheader("📕 Issue Book")


        if (
            len(books_df) > 0
            and len(members_df) > 0
        ):

            available_books = books_df[
                books_df["Status"] == "Available"
            ]


            if len(available_books) > 0:

                col1, col2 = st.columns(2)


                with col1:

                    selected_member = st.selectbox(
                        "Select Member",
                        members_df["Member ID"].tolist()
                    )


                with col2:

                    selected_book = st.selectbox(
                        "Select Book",
                        available_books["Book ID"].tolist()
                    )


                issue_date = st.date_input(
                    "Issue Date"
                )


                if st.button(
                    "📕 Issue Book",
                    type="primary"
                ):

                    if len(issues_df) == 0:

                        issue_id = "1"

                    else:

                        issue_id = str(
                            len(issues_df) + 1
                        )


                    books_df.loc[
                        books_df["Book ID"] == selected_book,
                        "Status"
                    ] = "Issued"


                    books_df.to_csv(
                        "books.csv",
                        index=False
                    )


                    new_issue = {
                        "Issue ID": issue_id,
                        "Book ID": selected_book,
                        "Member ID": selected_member,
                        "Issue Date": str(issue_date),
                        "Status": "Issued"
                    }


                    issues_df = pd.concat(
                        [
                            issues_df,
                            pd.DataFrame([new_issue])
                        ],
                        ignore_index=True
                    )


                    issues_df.to_csv(
                        "issues.csv",
                        index=False
                    )


                    st.success(
                        "✅ Book issued successfully!"
                    )


            else:

                st.info(
                    "No books are currently available."
                )


        else:

            st.info(
                "Please add at least one book "
                "and one member first."
            )


    # --------------------------------------------------------
    # Return Book
    # --------------------------------------------------------

    elif circulation_action == "Return Book":

        st.subheader("🔄 Return Book")


        issued_records = issues_df[
            issues_df["Status"] == "Issued"
        ]


        if len(issued_records) > 0:

            return_issue_id = st.selectbox(
                "Select Issue ID",
                issued_records["Issue ID"].tolist()
            )


            if st.button(
                "🔄 Return Book",
                type="primary"
            ):

                book_id = issued_records.loc[
                    issued_records["Issue ID"] == return_issue_id,
                    "Book ID"
                ].values[0]


                books_df.loc[
                    books_df["Book ID"] == book_id,
                    "Status"
                ] = "Available"


                books_df.to_csv(
                    "books.csv",
                    index=False
                )


                issues_df.loc[
                    issues_df["Issue ID"] == return_issue_id,
                    "Status"
                ] = "Returned"


                issues_df.to_csv(
                    "issues.csv",
                    index=False
                )


                st.success(
                    "✅ Book returned successfully!"
                )


        else:

            st.info(
                "No books are currently issued."
            )


# ============================================================
# REPORTS
# ============================================================

elif st.session_state.page == "Reports":

    st.markdown(
        '<div class="main-title">📊 Reports</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">'
        'Library statistics and records'
        '</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # Statistics
    # --------------------------------------------------------

    total_books = len(books_df)

    total_members = len(members_df)

    available_books = len(
        books_df[
            books_df["Status"] == "Available"
        ]
    )

    issued_books = len(
        books_df[
            books_df["Status"] == "Issued"
        ]
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "📚 Total Books",
            total_books
        )


    with col2:

        st.metric(
            "👥 Total Members",
            total_members
        )


    with col3:

        st.metric(
            "✅ Available",
            available_books
        )


    with col4:

        st.metric(
            "📕 Issued",
            issued_books
        )


    # --------------------------------------------------------
    # Category Report
    # --------------------------------------------------------

    st.subheader("📂 Books by Category")


    if len(books_df) > 0:

        category_report = (
            books_df["Category"]
            .value_counts()
            .reset_index()
        )

        category_report.columns = [
            "Category",
            "Number of Books"
        ]

        st.dataframe(
            category_report,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No book data available."
        )


    # --------------------------------------------------------
    # Issue Report
    # --------------------------------------------------------

    st.subheader("📕 Issue Records")


    if len(issues_df) > 0:

        st.dataframe(
            issues_df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No issue records available."
        )


# ============================================================
# Footer
# ============================================================

st.markdown(
    """
    <div class="footer">
        📚 BookTrack — Library Management System
        <br>
        Built with Python, Streamlit and Pandas
    </div>
    """,
    unsafe_allow_html=True
)