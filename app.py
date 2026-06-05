elif selected == "Process Calculator":
    st.markdown('<div class="section-title">Process Calculator</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="info-panel">
            <h2>Business Process Savings Calculator</h2>
            <p class="subtle">
                Estimate time savings, cost savings, and quality improvement for a repetitive workflow.
                The calculator is designed for business process analysis, automation planning, and operational reporting.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("### Input Assumptions")

        monthly_cases = st.number_input(
            "Cases processed per month",
            min_value=50,
            max_value=100000,
            value=1200,
            step=50
        )

        minutes_per_case = st.number_input(
            "Manual minutes per case",
            min_value=1,
            max_value=240,
            value=18,
            step=1
        )

        hourly_cost = st.number_input(
            "Average staff cost per hour",
            min_value=10,
            max_value=250,
            value=35,
            step=5
        )

        automation_rate = st.slider(
            "Automation coverage",
            min_value=5,
            max_value=95,
            value=45,
            step=5
        )

        error_rate_before = st.slider(
            "Current error rate",
            min_value=1,
            max_value=40,
            value=12,
            step=1
        )

        error_reduction = st.slider(
            "Expected error reduction",
            min_value=5,
            max_value=90,
            value=50,
            step=5
        )

    total_manual_hours = (monthly_cases * minutes_per_case) / 60
    automated_hours = total_manual_hours * (automation_rate / 100)
    remaining_manual_hours = total_manual_hours - automated_hours

    monthly_cost_before = total_manual_hours * hourly_cost
    monthly_cost_saved = automated_hours * hourly_cost
    annual_cost_saved = monthly_cost_saved * 12

    error_rate_after = error_rate_before * (1 - error_reduction / 100)
    errors_before = monthly_cases * (error_rate_before / 100)
    errors_after = monthly_cases * (error_rate_after / 100)
    errors_reduced = errors_before - errors_after

    if automation_rate >= 70:
        impact_level = "High impact"
        impact_badge = "badge-green"
    elif automation_rate >= 40:
        impact_level = "Moderate impact"
        impact_badge = "badge-orange"
    else:
        impact_level = "Early opportunity"
        impact_badge = "badge-purple"

    with col2:
        st.markdown("### Estimated Results")

        m1, m2 = st.columns(2)
        m1.metric("Manual Hours / Month", f"{total_manual_hours:,.0f}")
        m2.metric("Hours Saved / Month", f"{automated_hours:,.0f}")

        m3, m4 = st.columns(2)
        m3.metric("Monthly Cost Saved", f"${monthly_cost_saved:,.0f}")
        m4.metric("Annual Cost Saved", f"${annual_cost_saved:,.0f}")

        m5, m6 = st.columns(2)
        m5.metric("Errors Reduced / Month", f"{errors_reduced:,.0f}")
        m6.metric("Remaining Manual Hours", f"{remaining_manual_hours:,.0f}")

        st.markdown(
            f"""
            <div class="project-card">
                <h3>Impact Summary</h3>
                <p class="subtle">
                    Estimated monthly saving: <b>${monthly_cost_saved:,.0f}</b><br>
                    Estimated annual saving: <b>${annual_cost_saved:,.0f}</b>
                </p>
                <span class="{impact_badge}">{impact_level}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    comparison_data = pd.DataFrame({
        "Metric": [
            "Monthly manual hours",
            "Monthly labour cost",
            "Error rate",
            "Estimated errors per month"
        ],
        "Before": [
            round(total_manual_hours, 2),
            round(monthly_cost_before, 2),
            round(error_rate_before, 2),
            round(errors_before, 2)
        ],
        "After": [
            round(remaining_manual_hours, 2),
            round(monthly_cost_before - monthly_cost_saved, 2),
            round(error_rate_after, 2),
            round(errors_after, 2)
        ]
    })

    st.markdown('<div class="section-title">Before and After View</div>', unsafe_allow_html=True)

    st.dataframe(
        comparison_data,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Metric": st.column_config.TextColumn("Metric", width="medium"),
            "Before": st.column_config.NumberColumn("Before", format="%.2f"),
            "After": st.column_config.NumberColumn("After", format="%.2f"),
        }
    )

    fig = px.bar(
        comparison_data,
        x="Metric",
        y=["Before", "After"],
        barmode="group",
        title="Before and After Comparison",
        template="plotly_dark"
    )

    st.plotly_chart(plotly_layout(fig), use_container_width=True)

    result_csv = comparison_data.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Calculation Summary",
        data=result_csv,
        file_name="process_savings_summary.csv",
        mime="text/csv",
        use_container_width=True
    )
