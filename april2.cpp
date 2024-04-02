class Solution
{
    public:
    void inorder(Node *temp,int &ans,int &prev)
    {
        if(temp==NULL)
        {
        return;
        }
        inorder(temp->left,ans,prev);

        if(prev!=-1)
        ans=min(ans,abs(temp->data-prev));
        prev=temp->data;

        inorder(temp->right,ans,prev);
    }
    int absolute_diff(Node *root)
    {
           int ans=INT_MAX,prev=-1;
        inorder(root,ans,prev);
        return ans;
    }
};
