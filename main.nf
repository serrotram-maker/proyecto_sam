
params.file = "$HOME/main_py/WT.sam"
params.script = "$HOME/main_py/main.py"

process analyze_sam {
    publishDir "py_results/", mode: 'copy'
    input:
        path file
    output:
        file "output_WT_MAPQ60.txt"
    script:
    """
    uv run python ${params.script} ${file} > output_WT_MAPQ60.txt
    """
}
workflow {
    analyze_sam(params.file)
}
